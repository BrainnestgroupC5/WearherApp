import requests
import json
from datetime import datetime

API_KEY = "b723053f535f3dd2c853d68caf98ad54"
WEATHER_API_ENDPOINT = f"https://api.openweathermap.org/data/2.5/weather"

class WeatherDataService:

    def __init__(self):
        self.current_date = datetime.now().strftime("%H:%M - %d %B %Y ")
        
    def get_weather_data(self,city_name):

        weather_params = {
            "q":city_name,
            "appid":API_KEY
        }
        response  = requests.get(WEATHER_API_ENDPOINT, params=weather_params)
        source = response.text

        data = json.loads(source)

        return data