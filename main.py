import json


def load_data(file_path):
    """Load JSON data from a file."""
    with open(file_path, "r") as handle:
        return json.load(handle)


def read_template(file_path):
    """Read the HTML template from a file."""
    with open(file_path, "r") as fileobj:
        return fileobj.read()


def generate_output(animals_data):
    """Generate HTML output for the list of animals."""
    output = ""
    for item in animals_data:
        name = item.get("name")
        location = item["locations"][0]
        characteristics = item.get("characteristics", {})
        diet = characteristics.get("diet")
        animal_type = characteristics.get("type", "N/A")
        skin_type = characteristics.get("skin_type")
        lifespan = characteristics.get("lifespan")

        output += '<li class="cards__item">\n'
        output += f'<div class="card__title">{name}</div>\n'
        output += '<p class="card__text">\n'
        output += f"<strong>Location:</strong> {location}<br>\n"
        output += f"<strong>Diet:</strong> {diet}<br>\n"
        output += f"<strong>Skin_type:</strong> {skin_type}<br>\n"
        output += f"<strong>Lifespan:</strong> {lifespan}<br>\n"
        if animal_type != "N/A":
            output += f"<strong>Type:</strong> {animal_type}<br>\n"
        output += '</p>\n'
        output += '</li>\n'

    return output


def write_output_to_file(output, template, output_file_path):
    """Write the generated output to HTML file."""
    result = template.replace("__REPLACE_ANIMALS_INFO__", output)
    with open(output_file_path, "w") as file_obj:
        file_obj.write(result)


def main():
    """Main function to coordinate the workflow."""
    animals_data = load_data('animals_data.json')
    template = read_template("animals_template.html")
    output = generate_output(animals_data)
    write_output_to_file(output, template, "animals.html")


if __name__ == "__main__":
    main()
