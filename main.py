import json


def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)


with open("animals_template.html", "r") as fileobj:
    x = fileobj.read()


animals_data = load_data('animals_data.json')

output = ""
for item in animals_data:
    name = item.get("name")
    location = item["locations"][0]
    characteristics = item.get("characteristics", {})
    diet = characteristics.get("diet")
    animal_type = characteristics.get("type", "N/A")
    if animal_type == "N/A":
        output += '<li class="cards__item">'
        output += f"Name: {name}<br/>\n"
        output += f"Location: {location}<br/>\n"
        output += f"Diet: {diet}<br/>\n"
    else:
        output += '<li class="cards__item">'
        output += f"Name: {name}<br/>\n"
        output += f"Location: {location}<br/>\n"
        output += f"Diet: {diet}<br/>\n"
        output += f"Type: {animal_type}<br/>\n"
        output += '</li>\n'

s = x.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w") as file_obj:
    file_obj.write(s)
