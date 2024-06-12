import requests

OPEN_WEATHER_API_KEY = 'a77163f24622134a4f910ec858cf432e'

def get_preferred_units():
  global settings
  # 'metric' for Celsius or 'imperial' for Fahrenheit
  if 'temperature_units' in settings:
    if settings['temperature_units'] == 'Celsius':
      return 'metric'
    elif settings['temperature_units'] == 'Fahrenheit':
      return 'imperial'
  else:
    return 'metric'

def get_weather(city_name):
  base_url = "https://api.openweathermap.org/data/2.5/weather"
  params = {
      'q': city_name,
      'appid': OPEN_WEATHER_API_KEY,
      'units': get_preferred_units()
  }

  response = requests.get(base_url, params=params)

  if response.status_code == 200:
      data = response.json()
      # print(json.dumps(data, indent=4))
      return data
  else:
      return None

def display_weather_data(weather_data):
  main = weather_data['main']
  wind = weather_data['wind']
  weather_description = weather_data['weather'][0]['description']

  print(f"Temperature: {main['temp']}{'°C' if get_preferred_units() == 'Celsius' else '°F'}")
  print(f"Humidity: {main['humidity']}%")
  print(f"Pressure: {main['pressure']} hPa")
  print(f"Weather Description: {weather_description}")
  print(f"Wind Speed: {wind['speed']} m/s")
