import requests
from tkinter import *
import json
import tkinter as tk
from ttkwidgets.autocomplete import AutocompleteCombobox

from weather_service import WeatherService

BACKGROUND_COLOR = '#476FA5'
FOREGROUND_COLOR = 'white'
#Enter you api key, endpoint from the OpenWeatherMap dashboard
API_KEY = "9823f6782a5af246d038124b2ff5e8ac"
WEATHER_API_ENDPOINT = f"https://api.openweathermap.org/data/2.5/weather"

root =Tk()
city_value = StringVar()

weather_service = WeatherService()
#Initialize Window
def initialize_window():
    root.geometry("400x500") #size of the window by default
    root.title("Weather Forecast")
    root.configure(bg=BACKGROUND_COLOR)

def set_photo(weather_info):
    photo= weather_service.get_photo(weather_info)
    image_lab.configure(image=photo)
    image_lab.image = photo

def get_weather_info(city_name):
    # Get city name from user from the input field (later in the code)
    weather_params = {
            "q":city_name,
            "appid":API_KEY
        }

    response  = requests.get(WEATHER_API_ENDPOINT, params=weather_params)
    return json.loads(response.text)


def show_weather():
    city_name = city_value.get()
    weather_info = get_weather_info(city_name)
    #as per API documentation, if the cod is 200, it means that weather data was successfully fetched
    if weather_info['cod'] == 200:
        weather_data = weather_service.get_data(weather_info)
        set_photo(weather_info)

        temp_now.config(text= f"{weather_data.temp} °C")   

        weather = f"\nCity name: {city_name.title()}\nCurrent date: {weather_data.current_date}\nTemperature (Celsius): {weather_data.temp}°\nFeels like in (Celsius): {weather_data.feels_like_temp}°\nPressure: {weather_data.pressure} hPa\nWind Speed: {round(weather_data.wind_speed,2)} mph\nHumidity: {weather_data.humidity}%\nSunrise at {weather_data.sunrise_time} and Sunset at {weather_data.sunset_time}\nCloud: {weather_data.cloudy}%\nCurrently: {weather_data.description}"
    else:
        weather = f"\nWeather for '{city_name}' not found!\nKindly Enter valid City Name !!"

    text_field.config(text=weather)

initialize_window()

city_head = Label(root, text = 'Enter City Name', font = 'Arial 12 bold',bg=BACKGROUND_COLOR,fg=FOREGROUND_COLOR).pack(pady=10) 
 
with open("all_cities.csv", "r",encoding='utf-8-sig') as file:
    cities = file.read().splitlines()
    
inp_city = AutocompleteCombobox(root, textvariable = city_value,  width = 24, font='Arial 14 bold', completevalues=cities).pack()

Button(root, command = show_weather, text = "Check Weather", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)

weather_now = Label(root, text = "The Weather is: ", font = 'arial 12 bold',bg=BACKGROUND_COLOR,fg=FOREGROUND_COLOR).pack(pady=10)

image_lab = tk.Label(root,bg=BACKGROUND_COLOR)
image_lab.pack()

temp_now = Label(root, font = 'arial 20 bold',bg=BACKGROUND_COLOR,fg=FOREGROUND_COLOR)
temp_now.pack(side="top")

text_field = Label(root, width=46, height=15,bg=BACKGROUND_COLOR, fg=FOREGROUND_COLOR)
text_field.pack(side="top")

root.mainloop()
