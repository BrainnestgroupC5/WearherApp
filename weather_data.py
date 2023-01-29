
import requests
import json
from datetime import datetime

API_KEY = "b723053f535f3dd2c853d68caf98ad54"
LAT_and_LON_ENDPOINT = f"http://api.openweathermap.org/geo/1.0/direct"
WEATHER_API_ENDPOINT = f"https://api.openweathermap.org/data/2.5/weather"

class WeatherDataService:

    def __init__(self):
        self.current_date = datetime.now().strftime("%H:%M - %d %B %Y ")
        self.lat_of_city = ''
        self.lon_of_city = ''

    def get_lat_lon(self,city_name):

        lat_lon_params = {
            "q":city_name,
            "appid":API_KEY
        }
        lat_and_lon_response = requests.get(LAT_and_LON_ENDPOINT,params=lat_lon_params)
        lat_and_lon_data = lat_and_lon_response.json()
        self.lat_of_city = lat_and_lon_data[0]['lat']
        self.lon_of_city = lat_and_lon_data[0]['lon']
        
    def get_weather_data(self):

        weather_params = {
            "lat":self.lat_of_city,
            "lon":self.lon_of_city,
            "appid":API_KEY
        }
        response  = requests.get(WEATHER_API_ENDPOINT, params=weather_params)
        source = response.text

        data = json.loads(source)

        return data