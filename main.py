from dotenv import load_dotenv
import os

import streamlit as st

from handlers import dates_handler, weather_handler
from handlers.settings_handler import *

def check_weather(city):
	if not city:
		if 'default_location' not in settings:
			print(f"No default location found in your settings, Please set default location by menu option 1")
			return
		city = settings["default_location"]
	
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
	                     enumerate(settings.get('favorite_locations', []), start=1)]
	if locations_display:
		print("Your Favorite Locations:")
		for location in locations_display:
			print(f"{location}")
		index = input("Which location to check for weather? (Choose from the list): ")
		if index and index.isdigit and 0 < int(index) <= len(settings['favorite_locations']):
			check_weather(settings['favorite_locations'][int(index) - 1])
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
			set_default_location()
		elif choice == '3':
			set_temperature_units()
		elif choice == '4':
			add_favorite_location()
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
		current_dir = os.getcwd()
		st.title('Welcome')
		st.write('Please choose one of the options in the menu')
		st.image(f"{current_dir}/assets/weather-image.jpeg", caption="DALL-AI", width=850)
	
	
	elif menu == 'Your Current Settings':
		st.title('Your Current Settings')
		st.write('Welcome to Your Current Settings page!')
	elif menu == 'Set Default Location':
		st.title('Set Default Location')
		st.write('This is the Set Default Location page.')
	
	elif menu == 'Set Temperature Units':
		st.title('Set Temperature Units')
		st.write('This is the Set Temperature Units page!')
	
	

def main():
	if os.getenv('RUN_MODE') == 'streamlit':
		run_streamlit()
	else:
		run_terminal()

load_dotenv()
main()
