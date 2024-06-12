import json

settings = {}

def load_settings():
  global settings
  try:
    with open('settings.json', 'r') as f:
        settings = json.load(f)
  except FileNotFoundError:
    print("Settings file was not found.")
  except json.JSONDecodeError:
    print("Error decoding settings JSON.")

def show_settings():
  global settings
  print(f'This is your current settings: {settings}')

def save_settings():
  global settings
  with open('settings.json', 'w') as f:
    json.dump(settings, f, indent=4)

def set_default_location():
  global settings
  default_location = input("Enter default location: ")
  if default_location:
    settings['default_location'] = default_location
    save_settings()
    print(f'Default location set to: {default_location}')

def set_temperature_units():
  global settings
  temperature_units = input("Enter temperature units (Celsius or Farenheit): ")
  if temperature_units:
    settings['temperature_units'] = temperature_units
    save_settings()
    print(f'Temperature Units set to: {temperature_units}')
    show_settings()

def add_favorite_location():
  global settings
  favorite_location = input("Enter a new favorite location: ")
  if favorite_location:
    if 'favorite_locations' in settings:
      settings['favorite_locations'].append(favorite_location)
    else:
      settings['favorite_locations'] = [favorite_location]
    save_settings()
    print(f'Favorite location added: {favorite_location}')
    show_settings()
