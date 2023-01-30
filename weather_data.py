class WeatherData:
    def __init__(self,temp,
    feels_like_temp,
    pressure,
    humidity,
    wind_speed,
    sunrise,
    sunset,
    timezone,
    cloudy,
    description,
    sunrise_time,
    sunset_time,
    current_date) -> None:
        self.temp =temp 
        self.feels_like_temp =feels_like_temp 
        self.pressure =pressure 
        self.humidity =humidity 
        self.wind_speed =wind_speed 
        self.sunrise =sunrise 
        self.sunset =sunset 
        self.timezone =timezone 
        self.cloudy =cloudy 
        self.description =description 
        self.sunrise_time =sunrise_time 
        self.sunset_time =sunset_time 
        self.current_date =current_date 