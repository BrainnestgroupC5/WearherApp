from tkinter import *
from weather_data import WeatherDataService




data = WeatherDataService()
class View(Tk):
    
    def __init__(self):
        super().__init__()
        self.title('Weather Broadcast')
        self.geometry("700x500")

        self.city_entry = Entry(width=30)
        self.city_entry.insert(END, 'baku')
        self.city_entry.place(x=200, y=10)
        data.get_lat_lon(self.city_entry.get())
        
        self.search_frame()
        self.celsius = ''
        
        self.more_details(data=data.get_weather_data())
        self.temperature_label = Label(text=self.celsius, font=("Courier", 50))
        self.temperature_label.place(x=270, y=60)
        self.city_name = Label(text=self.city_entry.get().title())
        self.city_name.place(x=305, y=130)
        date_label = Label(text=data.current_date)
        date_label.place(x=260, y=150)
        
        
    def searcher(self,temp_label):
        self.celsius = f"{round(data.get_weather_data()['main']['temp']-273.15)}°C"
        data.get_lat_lon(self.city_entry.get())


    def search_frame(self):
        search_button = Button(text="Search",width=10, command=self.searcher(self.temperature_label))
        search_button.place(x=500, y=10)



    def more_details(self,data):  
        currently_label = Label(text=f"Currently:                        {data['weather'][0]['description']}")
        feels_like_label = Label(text=f"Feels like:                        {round(data['main']['feels_like']-273.15)}")
        wind_speed_label = Label(text=f"Wind speed:                   {data['wind']['speed']} mph")

        currently_label.place(x=250, y=280)
        feels_like_label.place(x=250, y=310)
        wind_speed_label.place(x=250, y=340)

    

    def main(self):
        self.mainloop()






    


