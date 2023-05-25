import pandas as pd
import requests
import json

url = "https://api.fbi.gov/wanted/v1/list"
success = True
page = 1

criminals_list = []

while success:
    params = {"page": page}  # We have to specify a page parameter as well
    response = requests.get(url, params=params)
    if response.status_code == 200:
        # Request was successful
        json_data = response.json()
        if len(json_data["items"]) == 0:
            break
        criminals_list.extend(json_data["items"])
        print(page)
        page += 1
    else:
        # Request was not successful
        success = False
        print("Error:", response.status_code)

criminals_df = pd.json_normalize(criminals_list, max_level=1, record_prefix="subjects_")

criminals_df.to_excel("static/data/criminals.xlsx")
'''
def select_first2(given_list):
    try:
        first = given_list[0]
    except:
        first = None
    try:
        second = given_list[1]
    except:
        second = None

    returned_list = [first, second]
    return returned_list


normalized_criminals_list = []
for item in criminals_list:
    # select first 2 image
    normalized_item = {
        "reward_min": item["reward_min"],
        "occupations": item["occupations"],
        "poster_classification": item["poster_classification"],
        "place_of_birth": item["place_of_birth"],
        "weight_max": item["weight_max"],
        "title": item["title"],
        "hair_raw": item["weight"],
        "weight": item["weight"],
        "weight_min": item["weight_min"],
        "alias1": select_first2(item["aliases"])[0],
        "alias2": select_first2(item["aliases"])[1],
        "image1": select_first2(item["images"])[0]["original"],
        "image2": select_first2(item["images"])[1]["original"],
        "age_range": item["age_range"],
        "person_classification": item["person_classification"],
        "race": item["race"],
        "reward_max": item["reward_max"],
        "scars_and_marks": item["scars_and_marks"],
        "publication": item["publication"],
        "eyes_raw": item["eyes_raw"],
        "languages1": select_first2(item["languages"])[0],
        "languages2": select_first2(item["languages"])[1],
        "nationality": item["nationality"],
        "status": item["status"],
        "dates_of_birth_used": select_first2(item["dates_of_birth_used"])[0],
        "eyes": item["eyes"],
        "subject1": select_first2(item["subjects"])[0],
        "subject2": select_first2(item["subjects"])[1],
        "race_raw": item["race_raw"],
        "sex": item["sex"],
        "hair": item["hair"],
        "possible_states": select_first2(item["possible_states"])[0],
        "description": item["description"]

    }
    print(normalized_item)
    normalized_criminals_list.append(normalized_item)
'''
