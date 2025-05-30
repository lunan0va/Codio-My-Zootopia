import json


def load_data(file_path):
    """Lädt Tierdaten aus einer JSON-Datei."""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def serialize_animal(animal_obj):
  """Serialisiert ein einzelnes Tierobjekt zu HTML."""
  name = animal_obj.get("name", "")
  characteristics = animal_obj.get("characteristics", {})
  taxonomy = animal_obj.get("taxonomy", {})
  diet = characteristics.get("diet")
  locations = animal_obj.get("locations", [])
  location = ", ".join(locations) if locations else None
  type_ = characteristics.get("type")
  lifespan = characteristics.get("lifespan")
  color = characteristics.get("color")
  top_speed = characteristics.get("top_speed")
  scientific_name = taxonomy.get("scientific_name")

  html = f'<li class="cards__item">'
  html += f'<div class="card__title">{name}</div>'
  html += '<p class="card__text">'
  if diet:
    html += f'<strong>Diet:</strong> {diet}<br/>'
  if location:
    html += f'<strong>Location:</strong> {location}<br/>'
  if type_:
    html += f'<strong>Type:</strong> {type_}<br/>'
  if lifespan:
    html += f'<strong>Lifespan:</strong> {lifespan}<br/>'
  if color:
    html += f'<strong>Color:</strong> {color}<br/>'
  if top_speed:
    html += f'<strong>Top Speed:</strong> {top_speed}<br/>'
  if scientific_name:
    html += f'<strong>Scientific Name:</strong> {scientific_name}<br/>'
  html += '</p></li>\n'
  return html


def generate_animal_cards(data):
    """Erzeugt HTML für alle Tierkarten."""
    return ''.join(serialize_animal(animal) for animal in data)


def create_html(data, template_path, output_path):
    """Erstellt die finale HTML-Datei mit den Tierkarten."""
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    cards_html = generate_animal_cards(data)
    final_html = template.replace("__REPLACE_ANIMALS_INFO__", cards_html)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_html)


if __name__ == "__main__":
    data = load_data("animals_data.json")
    create_html(data, "animals_template.html", "animals.html")
