import pandas as pd
import requests
import json

url = "https://akabab.github.io/superhero-api/api/all.json"

response = requests.get(url)
if response.status_code == 200:
    # Request was successful
    json_data = response.json()


heros_df = pd.json_normalize(json_data)

#heros_df.to_excel("static/data/heros.xlsx")

df = None

for column in heros_df:
    current = heros_df[column]
    for row in current:
        if isinstance(row, list):
            print(column, row)
            try:
                df3 = pd.DataFrame(heros_df[column].to_list(), columns=[column+str(i) for i in range(len(row))])
                print(df3)
                df = pd.concat([df, df3], axis=1, join="inner")
            except:
                pass
        break
# Adding the 'id' column directly
df['id'] = range(1, len(df) + 1)
print(df)
print(heros_df)

heros_df_merged = pd.merge(heros_df, df, on="id", how="right")
heros_df_merged.to_csv("static/data/superheroes.csv", index=False)

with open("static/data/superheroes.json", 'w') as file:
    json.dump(json_data, file)
