import streamlit as st
from datetime import datetime
import pytz

def display_date_time(user_timezone, location_timezone=None):
  print("\n")
  user_time = datetime.now(pytz.timezone(user_timezone))
  formatted_user_time = user_time.strftime("%A, %B %d, %Y, %I:%M %p")
  print(f"Your current date and time in {user_timezone}: {formatted_user_time}")

  if location_timezone:
    try:
      location_timezone = pytz.timezone(location_timezone)
    except pytz.UnknownTimeZoneError:
      print(f"Invalid timezone: {location_timezone}")
      return

    location_time = user_time.astimezone(pytz.timezone(location_timezone))
    formatted_location_time = location_time.strftime("%A, %B %d, %Y, %I:%M %p")
    print(f"Date and time in {location_timezone}: {formatted_location_time}")

def display_date_time_streamlit(user_timezone, location_timezone=None):
  user_time = datetime.now(pytz.timezone(user_timezone))
  formatted_user_time = user_time.strftime("%A, %B %d, %Y, %I:%M %p")
  st.write(f"Your current date and time in {user_timezone}: {formatted_user_time}")

  if location_timezone:
    try:
      location_timezone = pytz.timezone(location_timezone)
    except pytz.UnknownTimeZoneError:
      st.write(f"Invalid timezone: {location_timezone}")
      return

    location_time = user_time.astimezone(pytz.timezone(location_timezone))
    formatted_location_time = location_time.strftime("%A, %B %d, %Y, %I:%M %p")
    st.write(f"Date and time in {location_timezone}: {formatted_location_time}")
