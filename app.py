import requests
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

st.set_page_config(page_title="Weather App",page_icon='🌈')

st.title('Weather App')

st.write("Enter the city name and click on the button to get weather data")

city = st.text_input("Enter city name:")

API_URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
                                                               
if st.button("Fetch weather Data"):
  response = requests.get(API_URL)
  data = response.json()

  if response.status_code == 200:
  # Fetch the Weather data in variables
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    weather = data['weather'][0]['main']

    print(temperature,humidity,wind_speed,weather)

    st.metric("Temperature",f"🌡️{temperature}℃")
    st.metric("Humidity",F"💧{humidity}%")
    st.metric("Wind Speed",f"💨{wind_speed}m/s")
    st.metric("Weather",f"☁️{weather}")
  else:
    st.error("City not found please check the city name and region")  





