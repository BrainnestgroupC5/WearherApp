from PIL import Image, ImageTk
import urllib.request
from datetime import datetime, timedelta
import pytz

from weather_data import WeatherData

class WeatherService:

    def get_photo(self,weather_info):
        icon_id = weather_info['weather'][0]['icon']
        icon_url = f'http://openweathermap.org/img/wn/{icon_id}.png'
        res = urllib.request.urlopen(icon_url)
        img =Image.open(res).resize((80, 80))
        photo = ImageTk.PhotoImage(img)
        return photo
       
    def time_format_for_location(self,utc_with_tz):
        local_time = datetime.utcfromtimestamp(utc_with_tz)
        return local_time.time()


    def get_data(self,weather_info):
        kelvin = 273.15 # value of kelvin

        temp = int(weather_info['main']['temp'] - kelvin) #converting default kelvin value to Celcius
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] * 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']
        utc_with_tz = int(sunrise)  + int(timezone) 
        sunrise_time = self.time_format_for_location(utc_with_tz)
        utc_with_tz = int(sunset) +  int(timezone) 
        sunset_time = self.time_format_for_location(utc_with_tz)
        
        current_date = datetime.utcnow()+timedelta(seconds=timezone)
        formatted_current_date = current_date.strftime("%H:%M - %d/%m/%Y")
        

        return WeatherData(temp, feels_like_temp, pressure, humidity, wind_speed, sunrise, sunset, timezone, 
        cloudy, description, sunrise_time,sunset_time, formatted_current_date)

