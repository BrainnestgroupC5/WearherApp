# WeatherApp

# Weather application

It shows the current weather conditions and forecast for a specific location.

## Tech Stack

**Backend technologies:** 

- Python v3.10.x or higher,

- Libraries

    - requests
    - tkinter
    - json
    - ttk widgets.autocomplete
    - PIL
    - urllib.request
    - datetime
    - pytz



## About application

The project is divided to :

- weather_service.py :

    Aims to create local time of the specific location, the weather icon and the weather features such as temparature, humidity, wind speed and... It includes three function (get_photo, time_format_for_location, get_data). 

    - get_photo creates the icon figure. To load a photo from a url address we used urlopen method from urllib.request. Here class of ImageTk.PhotoImage from the ImageTk module is used to create compatible image for GUI. 

        - time_format_for_location : creats local time using utcfromtimestamp method from datetime module.
        - get_data : gets weather information for a specific location from OpenWeatherMap as input and then creates a class of weather features such as humidity, temparature and some time information such as sunset and sunrise time. 

- weather_data.py :

    To create the input in terms of class, another function called weather_data was created. which includes a weather class which covers all weather features and time features as above mentioned. 

- all_cities.csv : 

    Names of all exixting cities around the world were saved in a .csv file for autocomplete purpose, while the user enters the city name.

- weather_app.py :

- It is the main function.

    - We imported ttkwidgets.autocomplete which is a module from the ttkwidgets package, to make suggestion for autocompletion while entering the city name. 
    - requests was imported to get access to a specific url content.
    - tkinter module was imported to create a GUI.
    - json was imported to use loads() for conversion from a json file to a python object. 
    - Initialize_window function was created to define the specific properties of the GUI window such as its size or background color.
    - class of Weatherservice was imported from weather_service.py to produce the final output of the weather app. 
    - set_photo function was created to add the weather icon to the GUI. It calls the get_photo from Weatherservice to read the photo from url and set_photo get this photo as input to display it inside the GUI. 
    - get_weather_info function was created to produce the content of Openweathermap for a specific city. It gets the city name as input. 
    - show_weather function was created as a command for the Button which is here "Check Weather". When the button "Check Weather" is clicked, the show_weather will be executed. 
    
        Based on API documentation, if the cod of weather_info is 200, it means that weather data was successfully fetched. In case of successful fetch it will show the information such as temerature, Pressure , cloud and etc. If it wasnt successful then it shows "Weather for 'city_name' not found! Kindly Enter valid City Name" It will also shows temaparture in celesius in different location (almost center of the GUI window).

    - The GUI window is initialized with the specific parameters such as window size or background color.
    - The Label method was used to show the text "Enter the city name"
    - All the available cities' names were included in a .csv file inorder to use them for the autocomplete purpose.
    - AutocompleteCombobox was used to enable the user the autocomplete option and helps the user to select the city name from the drop down menu.
    - Label method was used to display "The weather is:" with a specific font, background and foreground color. 
    - The mainloop() method was used to keep the window open until it is closed.
 
    - The root.configure method in Tkinter is used to change the configuration options (such as color, font, text.) of a Tkinter widget.


