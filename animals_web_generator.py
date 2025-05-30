import json

def load_data(file_path):
  """ Load a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def generate_animal_info(data):
  output = ''
  for animal in data:
    name = animal.get("name")
    diet = animal.get("characteristics", {}).get("diet")
    locations = animal.get("locations", [])
    location = locations[0] if locations else None
    type_ = animal.get("characteristics", {}).get("type")

    if name:
      output += f"Name: {name}\n"
    if diet:
      output += f"Diet: {diet}\n"
    if location:
      output += f"Location: {location}\n"
    if type_:
      output += f"Type: {type_}\n"

    output += "\n"
  return output

def create_html(data, template_path, output_path):

  with open(template_path, "r") as f:
    html_template = f.read()

  animal_info = generate_animal_info(data)
  final_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animal_info)

  with open(output_path, "w") as f:
    f.write(final_html)


if __name__ == "__main__":
  animals_data = load_data("animals_data.json")
  create_html(animals_data, "animals_template.html", "animals.html")
