from geopy.geocoders import Nominatim
import pandas as pd
import pycountry
import json

cities = pd.read_csv('static/data/criminals_cities.csv')

# Geocoding service (Nominatim in this example)
# geolocator = Nominatim(user_agent="city_country_lookup")
geolocator = Nominatim(user_agent="city_to_country")

country_names = []
country_codes_a2 = []
country_codes_a3 = []
city_names = []
latitudes = []
longitudes = []


# Iterate over each city
for city in cities.itertuples():
    location = geolocator.geocode(city.place_of_birth, exactly_one=True, addressdetails=True)


    if location is not None:
        country_code_a2 = location.raw['address'].get('country_code')
        if ',' in city.place_of_birth:
            city_name = city.place_of_birth.split(",")[0]
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

        country_names.append(country_name)
        country_codes_a2.append(country_code_a2)
        country_codes_a3.append(country_code_a3)
        city_names.append(city_name)
        latitudes.append(latitude)
        longitudes.append(longitude)

        print(f"The city {city_name} is in {country_name} ({country_code_a3}).")
    else:
        #print(f"The city {city.place_of_birth} was not found.")
        country_names.append(None)
        country_codes_a2.append(None)
        country_codes_a3.append(None)
        city_names.append(None)
        latitudes.append(None)
        longitudes.append(None)

cities["country_names"] = country_names
cities["country_codes_a2"] = country_codes_a2
cities["country_codes_a3"] = country_codes_a3
cities["city_name"] = city_names
cities["longitude"] = longitude
cities["latitude"] = latitude

cities.to_csv('static/data/criminals_cities.csv')

