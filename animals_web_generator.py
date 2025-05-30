import json

def load_data(file_path):
  """ Load a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

for animal in animals_data:
  print(f"Name: {animal.get('name')}")

  characteristics = animal.get("characteristics", {})

  if "diet" in characteristics:
    print(f"Diet: {characteristics['diet']}")

  if "locations" in animal and animal["locations"]:
    print(f"Location: {animal['locations'][0]}")

  if "type" in characteristics:
    print(f"Type: {characteristics['type']}")

  print()