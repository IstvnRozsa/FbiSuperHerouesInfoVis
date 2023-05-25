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

for column in heros_df:
    current = heros_df[column]
    for row in current:
        if isinstance(row, list):
            print(column, row)
            try:
                df3 = pd.DataFrame(heros_df[column].to_list(), columns=[column+str(i) for i in range(len(row))])
                print(df3)
            except:
                pass
        break