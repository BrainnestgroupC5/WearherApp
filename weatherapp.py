import requests
from tkinter import *
import json
import tkinter as tk
from io import BytesIO
import io

from weather_service import WeatherService

BACKGROUND_COLOUR ='#476FA5'
FOREGROUND_COLOUR ='white'
#Enter you api key, copies from the OpenWeatherMap dashboard
API_KEY = "9823f6782a5af246d038124b2ff5e8ac"  #sample API
WEATHER_API_ENDPOINT = f"https://api.openweathermap.org/data/2.5/weather"

root =Tk()
city_value = StringVar()

weather_service = WeatherService()
#Initialize Window
def initialize_window():
    root.geometry("400x500") #size of the window by default
    root.resizable(0,0) #to make the window size fixed
    root.title("Weather Forecast")#title of our window
    root.configure(background=BACKGROUND_COLOUR)

def set_photo(weather_info):
    photo= weather_service.get_photo(weather_info)
    imagelab.configure(image=photo)
    imagelab.image = photo

def get_weather_info(city_name):
    # Get city name from user from the input field (later in the code)
    weather_params = {
            "q":city_name,
            "appid":API_KEY
        }

    response  = requests.get(WEATHER_API_ENDPOINT, params=weather_params)
    return json.loads(response.text)


def showWeather():
    city_name = city_value.get()
    weather_info = get_weather_info(city_name)
    #as per API documentation, if the cod is 200, it means that weather data was successfully fetched
    if weather_info['cod'] == 200:
        weather_data =weather_service.get_data(weather_info)
        set_photo(weather_info)
        temp_now.pack()
        #assigning Values to our weather varaible, to display as output
        temp_now.config(text= f"{weather_data.temp}°")   #to insert or send value in our Text Field to display output
        weather = f"\nWeather of: {city_name.title()}\nCurrent date: {weather_data.current_date}\nTemperature (Celsius): {weather_data.temp}°\nFeels like in (Celsius): {weather_data.feels_like_temp}°\nPressure: {weather_data.pressure} hPa\nWind Speed: {round(weather_data.wind_speed,2)}mph\nHumidity: {weather_data.humidity}%\nSunrise at {weather_data.sunrise_time} and Sunset at {weather_data.sunset_time}\nCloud: {weather_data.cloudy}%\nInfo: {weather_data.description}"
    else:
        weather = f"\nWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"

    tfield.config(text=weather)   #to insert or send value in our Text Field to display output
    #::::::::::::::::::::::::::

initialize_window()

#::::::::::::::::::::::::::
city_head= Label(root, text = 'Enter City Name', font = 'Arial 12 bold',background=BACKGROUND_COLOUR,foreground=FOREGROUND_COLOUR).pack(pady=10) #to generate label heading
 
inp_city = Entry(root, textvariable = city_value,  width = 24, font='Arial 14 bold').pack() #entry field
#:::::::::::::::::::::::::
Button(root, command = showWeather, text = "Check Weather", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
#:::::::::::::::::::::::::::
weather_now = Label(root, text = "The Weather is: ", font = 'arial 12 bold',background=BACKGROUND_COLOUR,foreground=FOREGROUND_COLOUR).pack(pady=10)
imagelab = tk.Label(root,background=BACKGROUND_COLOUR)
imagelab.pack()



temp_now = Label(root, font = 'arial 20 bold',background=BACKGROUND_COLOUR,foreground=FOREGROUND_COLOUR)
temp_now.pack(side="top")

tfield = Label(root, width=46, height=15,background=BACKGROUND_COLOUR, foreground=FOREGROUND_COLOUR)
tfield.pack(side="top")

#:::::::::::::::::
root.mainloop()
