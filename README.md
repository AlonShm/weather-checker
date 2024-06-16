# weather-checker
Python Project: Weather Checker Application

The application is available on Streamlit service and can be accessed by this URL:

https://weather-checker-hjgtfmfvfs9au4p6wyvx8x.streamlit.app/

# This application supports two running modes : 
*Terminal*

* Set RUN_MODE .env parameter to terminal 
* Run command: python3 main.py
* Choose one of the menu options:
   1. Your Current Settings
   2. Set Default Location
   3. Set Temperature Units
   4. Add Favorite Location
   5. Check Weather For Favorites
   6. Check Weather For A New or Default Location
   7. Exit


*streamlit*
* Set .env parameter to streamlit
* Run command: poetry shell
* Run command: streamlit run main.py
* Use you browser and set this url: http://localhost:8502
* When the application is loaded you'll have the welcome screen together with a user-friendly menu with all the available options.
* Enjoy!

*** You already have a settings file as default and can add more settings by using the menu options


# Project Structure
- colab-notebook - contains colab notebook with the same functionality as the pycharm project

- handlers - contains handler python file for each main logic in the application: dates, settings, weather fetch

- resources - contains the settings json file

- main.py - application starting point

- .env - environment variable for the App. Currently holds the RUN_MODE only
