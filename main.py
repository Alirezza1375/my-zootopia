import json
import os

def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')


for item in animals_data:
    name = item.get("name")
    characteristics = item.get("characteristics", {})
    location = item["locations"][0]
    diet = characteristics.get("diet")
    animal_type = characteristics.get("type", "N/A")

    if animal_type == "N/A":
        print(f"Name: {name}\nDiet: {diet}\nlocation: {location}\n")
    else:
        print(f"Name: {name}\nDiet: {diet}\nlocation: {location}\nType: {animal_type}\n")
















