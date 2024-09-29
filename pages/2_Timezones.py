import pytz
import streamlit as st
from datetime import datetime

timezones = list(pytz.all_timezones_set)
abbreviations = {}


def get_keys_from_value(dictionary, target_value):
    keys = [key for key, value in dictionary.items() if value == target_value]
    return keys


for tz in timezones:
    timezone = pytz.timezone(tz)
    current_time = datetime.now(timezone)
    abbreviations[tz] = current_time.strftime('%Z')


def take_time():
    obj = datetime.now()
    tz = pytz.timezone(get_keys_from_value(abbreviations, from_time_zone)[0])
    obj = tz.localize(obj)
    new_tz = pytz.timezone(get_keys_from_value(abbreviations, to_time_zone)[0])
    new_tz_time = datetime.strftime(obj.astimezone(new_tz), "%H:%M:%S")
    time.markdown(f"## {new_tz_time}")


time = st.empty()
col1, col2 = st.columns(2)
from_time_zone = col1.selectbox("Convert from which timezone?", options=abbreviations.values())
to_time_zone = col2.selectbox("Convert to which timezone?", options=abbreviations.values())

while True:
    take_time()
