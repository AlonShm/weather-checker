import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import os

from handlers import dates_handler, weather_handler
from handlers.settings_handler import *

def check_weather(city):
	if not city:
		if 'default_location' not in get_settings():
			print(f"No default location found in your settings, Please set default location by menu option 1")
			return
		city = get_settings()["default_location"]
	
	weather_data = weather_handler.get_weather(city)
	
	if weather_data:
		dates_handler.display_date_time("Israel", city)
		print("\n")
		print(f"The weather conditions in {city}:")
		weather_handler.display_weather_data(weather_data)
	else:
		print("Failed to retrieve data")

def check_weather_for_favorite_location():
	locations_display = [f"{index}. {location}"
	                     for index, location in
	                     enumerate(get_settings().get('favorite_locations', []), start=1)]
	if locations_display:
		print("Your Favorite Locations:")
		for location in locations_display:
			print(f"{location}")
		index = input("Which location to check for weather? (Choose from the list): ")
		if index and index.isdigit and 0 < int(index) <= len(get_settings()['favorite_locations']):
			check_weather(get_settings()['favorite_locations'][int(index) - 1])
		else:
			print("Invalid choice")
	else:
		print("No favorite locations found in your settings")
		
def run_terminal():
	load_settings()
	while True:
		print("\nWeather Checker Application")
		print("\nMain Menu:")
		print("1. Your Current Settings")
		print("2. Set Default Location")
		print("3. Set Temperature Units")
		print("4. Add Favorite Location")
		print("5. Check Weather For Favorites")
		print("6. Check Weather For A New or Default Location")
		print("7. Exit")
		choice = input("Enter your choice: ")
		
		if choice == '1':
			show_settings()
		elif choice == '2':
			default_location = input("Enter default location: ")
			set_default_location(default_location)
		elif choice == '3':
			temperature_units = input("Enter temperature units (Celsius or Farenheit): ")
			set_temperature_units(temperature_units)
		elif choice == '4':
			favorite_location = input("Enter a new favorite location: ")
			add_favorite_location(favorite_location)
		elif choice == '5':
			check_weather_for_favorite_location()
		elif choice == '6':
			city = input("Enter a city name: ")
			check_weather(city)
		elif choice == '7':
			print("See you next time.")
			break
		else:
			print("Invalid choice. Please try again.")
			
def run_streamlit():
	st.markdown("<h1 style='text-align: right;'>Weather Checker Application</h1>", unsafe_allow_html=True)
	
	menu = st.sidebar.selectbox(
		'Available Options:',
		['Welcome',
		 'Your Current Settings',
		 'Set Default Location',
		 'Set Temperature Units',
		 'Add Favorite Location',
		 'Check Weather For Favorites',
		 'Check Weather For A New or Default Location']
	)
	
	if menu == 'Welcome':
		st.title('Welcome')
		st.write('Please choose one of the options in the menu')
		st.image("resources/weather-image.jpeg", caption="DALL-AI", width=850)
	
	elif menu == 'Your Current Settings':
		st.title('Your Current Settings')
		if get_settings():
			df = pd.json_normalize(get_settings())
			if df.empty:
				st.write('You did not set any settings yet')
			st.dataframe(df)
		else:
			st.write("No settings file was found")
			
	elif menu == 'Set Default Location':
		st.title('Set Default Location')
		default_location = st.text_input("Enter default location:")
		if st.button("Save"):
			set_default_location(default_location)
			st.write(f'Default location set to: {default_location}')
	
	elif menu == 'Set Temperature Units':
		st.title('Set Temperature Units')
		temperature_units = st.text_input("Enter temperature units (Celsius or Farenheit):")
		if st.button("Save"):
			set_temperature_units(temperature_units)
			st.write(f'Temperature Units set to {temperature_units}')
			
	elif menu == 'Add Favorite Location':
		st.title('Add Favorite Location')
		favorite_location = st.text_input("Enter a new favorite location:")
		if st.button("Save"):
			add_favorite_location(favorite_location)
			st.write(f'Favorite location added: {favorite_location}')
	
	elif menu == 'Check Weather For Favorites':
		st.title('Check Weather For Favorites')
		if get_settings() and 'favorite_locations' in get_settings():
			setting_keys = ['-- Please Select --'] + list(get_settings()['favorite_locations'])
			selected_favorite = st.selectbox('Which location to check for weather? (Choose from the list):', setting_keys)
			
			if selected_favorite != '-- Please Select --':
				weather_data = weather_handler.get_weather(selected_favorite)
			
				if weather_data:
					dates_handler.display_date_time_streamlit("Israel", selected_favorite)
					st.write("\n")
					st.title(f"The weather conditions in {selected_favorite}:")
					weather_handler.display_weather_data_streamlit(weather_data)
				else:
					st.write("Failed to retrieve weather data")
		else:
			st.write("No settings file was found")
		
	elif menu == 'Check Weather For A New or Default Location':
		st.title('Check Weather For A New or Default Location')
		city = st.text_input("Enter city name (or leave empty for default location):")
		
		if st.button("Check"):
			if not city:
				if 'default_location' not in get_settings():
					st.write("No default location found in your settings, Please set default location by menu option")
					return
				city = get_settings()["default_location"]
			
			weather_data = weather_handler.get_weather(city)
				
			if weather_data:
				dates_handler.display_date_time_streamlit("Israel", city)
				st.write("\n")
				st.title(f"The weather conditions in {city}:")
				weather_handler.display_weather_data_streamlit(weather_data)
			else:
				st.write("Failed to retrieve weather data")

def main():
	load_settings()
	if os.getenv('RUN_MODE') == 'streamlit':
		run_streamlit()
	else:
		run_terminal()

load_dotenv()
main()
