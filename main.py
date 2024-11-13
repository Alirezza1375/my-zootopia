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
    skin_type = characteristics.get("skin_type")
    lifespan = characteristics.get("lifespan")
    if animal_type == "N/A":
        output += '<li class="cards__item">\n'
        output += f'<div class="card__title">{name}</div>\n'
        output += '<p class="card__text">\n'
        output += f"<strong>Location:</strong> {location}<br>\n"
        output += f"<strong>Diet:</strong> {diet}<br>\n"
        output += f"<strong>Skin_type:</strong> {skin_type}<br>\n"
        output += f"<strong>Lifespan:</strong> {lifespan}<br>\n"
        output += '</p>\n'
        output += '</li>\n'
    else:
        output += '<li class="cards__item">\n'
        output += f'<div class="card__title">{name}</div>\n'
        output += '<p class="card__text">\n'
        output += f"<strong>Location:</strong> {location}<br>\n"
        output += f"<strong>Diet:</strong> {diet}<br>\n"
        output += f"<strong>Type:</strong> {animal_type}<br>\n"
        output += f"<strong>Skin_type:</strong> {skin_type}<br>\n"
        output += f"<strong>Lifespan:</strong> {lifespan}<br>\n"
        output += '</p>\n'
        output += '</li>\n'


s = x.replace("__REPLACE_ANIMALS_INFO__", output)


with open("animals.html", "w") as file_obj:
    file_obj.write(s)
