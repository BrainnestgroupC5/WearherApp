from tkinter import *
from weather_data import WeatherDataService




weather_data_service = WeatherDataService()
class View(Tk):
    
    def __init__(self):
        super().__init__()
        self.title('Weather Broadcast')
        self.geometry("700x500")

        self.city_entry = Entry(width=30)
        # i just inserted a city name for not getting error(it will shown first time when we open gui in the search field.).in the future i am planning to use city name as per user's location when it is open
        self.city_entry.insert(END, 'warsaw')
        self.city_entry.place(x=200, y=10)

        data = weather_data_service.get_weather_data(self.city_entry.get())

        # that is for search button
        self.search_frame()
        # in our api it shows temp as kelvin,therefore i used -273.15 to get celsius
        self.celsius = round(data['main']['temp']-273.15)
        
        self.more_details(data=data)

        self.temperature_label = Label(text=self.celsius, font=("Courier", 50))
        self.temperature_label.place(x=270, y=60)

        self.city_name_label = Label(text=self.city_entry.get().title())
        self.city_name_label.place(x=305, y=130)

        date_label = Label(text=weather_data_service.current_date)
        date_label.place(x=260, y=150)
        

    def search_frame(self):
        search_button = Button(text="Search",width=10,)
        search_button.place(x=500, y=10)



    def more_details(self,data):  
        # i have used more space on that,it can look weird.instead of this you should create another labels in gui for these datas.
        currently_label = Label(text=f"Currently:                        {data['weather'][0]['description']}")
        feels_like_label = Label(text=f"Feels like:                        {round(data['main']['feels_like']-273.15)}")
        wind_speed_label = Label(text=f"Wind speed:                   {data['wind']['speed']} mph")

        currently_label.place(x=250, y=280)
        feels_like_label.place(x=250, y=310)
        wind_speed_label.place(x=250, y=340)

    

    def main(self):
        self.mainloop()






    


