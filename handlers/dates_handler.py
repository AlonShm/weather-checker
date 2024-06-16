import streamlit as st
from datetime import datetime
import pytz

city_to_timezone = {
    'Tel Aviv': 'Asia/Jerusalem',
    'New York': 'America/New_York',
    'Los Angeles': 'America/Los_Angeles',
    'Chicago': 'America/Chicago',
    'London': 'Europe/London',
    'Paris': 'Europe/Paris',
    'Berlin': 'Europe/Berlin',
    'Tokyo': 'Asia/Tokyo',
    'Sydney': 'Australia/Sydney',
    'Melbourne': 'Australia/Melbourne',
    'Toronto': 'America/Toronto',
    'Vancouver': 'America/Vancouver',
    'Moscow': 'Europe/Moscow',
    'Beijing': 'Asia/Shanghai',
    'Shanghai': 'Asia/Shanghai',
    'Hong Kong': 'Asia/Hong_Kong',
    'Singapore': 'Asia/Singapore',
    'Dubai': 'Asia/Dubai',
    'Mumbai': 'Asia/Kolkata',
    'Delhi': 'Asia/Kolkata',
    'Bangkok': 'Asia/Bangkok'
}

def display_date_time(user_timezone, city=None):
  print("\n")
  user_time = datetime.now(pytz.timezone(user_timezone))
  formatted_user_time = user_time.strftime("%A, %B %d, %Y, %I:%M %p")
  print(f"Your current date and time in {user_timezone}: {formatted_user_time}")

  if city:
    try:
      timezone_name = city_to_timezone.get(city)
      location_timezone = pytz.timezone(timezone_name)
    except pytz.UnknownTimeZoneError:
      print(f"Invalid timezone: {city}")
      return

    location_time = user_time.astimezone(location_timezone)
    formatted_location_time = location_time.strftime("%A, %B %d, %Y, %I:%M %p")
    print(f"Date and time in {location_timezone}: {formatted_location_time}")

def display_date_time_streamlit(user_timezone, city=None):
  user_time = datetime.now(pytz.timezone(user_timezone))
  formatted_user_time = user_time.strftime("%A, %B %d, %Y, %I:%M %p")
  st.write(f"Your current date and time in {user_timezone}: {formatted_user_time}")

  if city:
    try:
      timezone_name = city_to_timezone.get(city)
      location_timezone = pytz.timezone(timezone_name)
    except pytz.UnknownTimeZoneError:
      st.write(f"Invalid timezone: {city}")
      return

    location_time = user_time.astimezone(location_timezone)
    formatted_location_time = location_time.strftime("%A, %B %d, %Y, %I:%M %p")
    st.write(f"Date and time in {location_timezone}: {formatted_location_time}")
