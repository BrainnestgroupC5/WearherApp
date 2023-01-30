import requests
from tkinter import *
import json
from datetime import datetime
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO
import urllib.request
import io


#Initialize Window
 
root =Tk()
root.geometry("400x500") #size of the window by default
root.resizable(0,0) #to make the window size fixed
#title of our window
root.title("Weather Forecast")
#::::::::::::::::::::::::::::::::
city_value = StringVar()

def showWeather():
 
#Enter you api key, copies from the OpenWeatherMap dashboard
    api_key = "9823f6782a5af246d038124b2ff5e8ac"  #sample API
    weather_api_endpoint = f"https://api.openweathermap.org/data/2.5/weather"
 
    # Get city name from user from the input field (later in the code)
    city_name=city_value.get()

    weather_params = {
            "q":city_name,
            "appid":api_key
        }
    response  = requests.get(weather_api_endpoint, params=weather_params)
    source = response.text

    weather_info = json.loads(source)

    # icon = weather_info['weather'][0]['icon']
    # icon_url = 'https://openweathermap.org/img/wn/'+icon+'@2x.png'
    # res = urllib.request.urlopen(icon_url)
    # image_data = res.read()
    # img = Image.open(io.BytesIO(image_data))
    # photo = ImageTk.PhotoImage(img)
    # label = Label(root, image = photo)
    # label.pack()
        
 
#as per API documentation, if the cod is 200, it means that weather data was successfully fetched
    
 
    if weather_info['cod'] == 200:
        kelvin = 273.15 # value of kelvin
 
#-----------Storing the fetched values of weather of a city
        
        temp = int(weather_info['main']['temp'] - kelvin)                                     #converting default kelvin value to Celcius
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] * 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']
 
        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)
        current_date = datetime.now().strftime("%H:%M - %d %B %Y ")
        

 
#assigning Values to our weather varaible, to display as output
         
        weather = f"\nWeather of: {city_name.title()}\nCurrent date: {current_date}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nWind Speed: {round(wind_speed,2)}mph\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"
    
 
 
 
    tfield.config(text=weather)   #to insert or send value in our Text Field to display output
    #::::::::::::::::::::::::::
def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()

#::::::::::::::::::::::::::
city_head= Label(root, text = 'Enter City Name', font = 'Arial 12 bold').pack(pady=10) #to generate label heading
 
inp_city = Entry(root, textvariable = city_value,  width = 24, font='Arial 14 bold').pack() #entry field
#:::::::::::::::::::::::::
Button(root, command = showWeather, text = "Check Weather", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
#:::::::::::::::::::::::::::
weather_now = Label(root, text = "The Weather is: ", font = 'arial 12 bold').pack(pady=10)

tfield = Label(root, width=46, height=20)
tfield.pack()


#:::::::::::::::::
root.mainloop()
