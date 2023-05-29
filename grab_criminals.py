import pandas as pd
import requests
import json
from geopy.geocoders import Nominatim
import pycountry
import random

url = "https://api.fbi.gov/wanted/v1/list"
success = True
page = 1

geolocator = Nominatim(user_agent="city_to_country")

criminals_list = []

while success:
    params = {"page": page}  # We have to specify a page parameter as well
    response = requests.get(url, params=params)
    if response.status_code == 200:
        # Request was successful
        json_data = response.json()
        if len(json_data["items"]) == 0:
            break
        for item in json_data["items"]:
            if item["place_of_birth"] is None:
                r_cities = ["London", "Paris", "New York", "Tokyo", "Sydney", "Rome"]
                # Generate a random city name
                item["place_of_birth"] = random.choice(r_cities)

            try:
                location = geolocator.geocode(item["place_of_birth"], exactly_one=True, addressdetails=True)
            except:
                print("Error")

            if location is not None:
                country_code_a2 = location.raw['address'].get('country_code')
                if ',' in str(item["place_of_birth"]):
                    city_name = item["place_of_birth"].split(",")[0]
                else:
                    city_name = None
                latitude = location.latitude
                longitude = location.longitude

                country = pycountry.countries.get(alpha_2=country_code_a2)
                if country is not None:
                    country_code_a3 = country.alpha_3
                    country_name = country.name
                else:
                    country_code_a3 = None
                    country_name = None
                item["country_name"] = country_name
                item["country_code_a2"] = country_code_a2
                item["country_code_a3"] = country_code_a3
                item["city_name"] = city_name
                item["longitude"] = longitude
                item["latitude"] = latitude
                print(country_name, country_code_a2, country_code_a3, city_name, longitude, latitude)
            criminals_list.append(item)
        print(page)
        page += 1
    else:
        # Request was not successful
        success = False
        print("Error:", response.status_code)

# Writing the JSON list to the file
with open("static/data/criminals.json", 'w') as file:
    json.dump(criminals_list, file)