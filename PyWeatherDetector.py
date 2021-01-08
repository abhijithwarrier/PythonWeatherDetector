# Programmer - python_scripts (Abhijith Warrier)

# PYTHON GUI SCRIPT TO FIND THE CURRENT WEATHER OF ANY CITY USING API KEY

# Create an account in https://openweathermap.org/ to get your Free API Key

# Importing necessary packages
import json
import requests
import tkinter as tk
from tkinter import *
from tkinter import messagebox

# Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidgets():
    cityLabel = Label(root, text="ENTER CITY NAME : ", bg="darkslategray4")
    cityLabel.grid(row=0, column=0, padx=10, pady=5)
    cityEntry = Entry(root, width=36, textvariable=cityName)
    cityEntry.grid(row=0, column=1, padx=10, pady=5)

    findButton = Button(root, text="FIND WEATHER", command=findWeather)
    findButton.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

    clearButton = Button(root, text="CLEAR", command=clearEntries)
    clearButton.grid(row=1, column=1, padx=5, pady=5, columnspan = 2)

    cityCoord = Label(root, text="CITY COORDINATES : ", bg="darkslategray4")
    cityCoord.grid(row=2, column=0, padx=10, pady=5)
    root.cityCoord = Entry(root, width=36)
    root.cityCoord.grid(row=2, column=1, padx=10, pady=5)

    tempLabel = Label(root, text="TEMPARATURE : ", bg="darkslategray4")
    tempLabel.grid(row=3, column=0, padx=10, pady=5)
    root.tempEntry = Entry(root, width=36)
    root.tempEntry.grid(row=3, column=1, padx=10, pady=5)

    humidityLabel = Label(root, text="HUMIDITY : ", bg="darkslategray4")
    humidityLabel.grid(row=4, column=0, padx=10, pady=5)
    root.humidityEntry = Entry(root, width=36)
    root.humidityEntry.grid(row=4, column=1, padx=10, pady=5)

    windLabel = Label(root, text="WIND : ", bg="darkslategray4")
    windLabel.grid(row=5, column=0, padx=10, pady=5)
    root.windEntry = Entry(root, width=36)
    root.windEntry.grid(row=5, column=1, padx=10, pady=5)

    pressureLabel = Label(root, text="ATMOSPHERIC PRESSURE : ", bg="darkslategray4")
    pressureLabel.grid(row=6, column=0, padx=10, pady=5)
    root.pressureEntry = Entry(root, width=36)
    root.pressureEntry.grid(row=6, column=1, padx=10, pady=5)

    descLabel = Label(root, text="WEATHER DESCRIPTION : ", bg="darkslategray4")
    descLabel.grid(row=7, column=0, padx=10, pady=5)
    root.descEntry = Entry(root, width=36)
    root.descEntry.grid(row=7, column=1, padx=10, pady=5)

# Defining findWeather() function to find the weather of the user-input city
def findWeather():
    # Storing the API KEY
    APIKey = "YOUR API KEY"
    # Storing the Weather URL (base URL) to which the request has to be sent
    weatherURL = "http://api.openweathermap.org/data/2.5/weather?"
    # Fetching the user-input city name
    cityname = cityName.get()
    # Concatenating API Key and user-input city name with weatherURL(base URL)
    # and storing the complete URL in requestURL
    # Setting units=metric means temparture will be shown in CELCIUS
    requestURL = weatherURL+"appid="+APIKey+"&q="+cityname+"&units=metric"
    # Sending the request to URL & Fetching and Storing the response
    response = requests.get(requestURL)
    # Converting response which is in json format data into Python Format
    weatherResponse = response.json()
    # Printing the weatherResponse dictionary.
    print(json.dumps(weatherResponse, indent=2))
    # Some values from the above weatherReponse dictionary will be fetched &
    # displayed in the tkinter window

    # Checking if the value of is not equal to 404
    if weatherResponse["cod"] != "404":
        # Fetching and Storing the value of "main" key from weatherResponse
        weatherPARA = weatherResponse["main"]
        # Fetching and Storing the value of "coord" key from weatherResponse
        coordinates = weatherResponse["coord"]
        # Storing the latitude and longitude key values from coordinates
        latitude = str(coordinates["lat"])
        longitude = str(coordinates["lon"])
        # Fetching and Storing the value of "wind" key from weatherResponse
        wind = weatherResponse["wind"]
        # Storing the speed key value from wind
        windSpeed = str(wind['speed'])
        # Checkif 'deg' key is present in 'wind' key of weatherResponse dict
        if 'deg' in wind.keys():
            windDirect = str(wind['deg'])
        # If not present, then set windDirect to empty string
        else:
            windDirect = ''

        # Fetching and Storing the temparature value from weatherPARA
        temperature = str(weatherPARA["temp"])
        # Fetching and Storing the pressure value from weatherPARA
        pressure = str(weatherPARA["pressure"])
        # Fetching and Storing the humidity value from weatherPARA
        humidiy = str(weatherPARA["humidity"])
        # Fetching and Storing weather value which is a list from weatherResponse
        weatherDesc = weatherResponse["weather"]
        # Storing the description value from 0 index item of weatherDesc list
        weatherDescription = weatherDesc[0]["description"]

        # Clearing previous weather entries if there's any
        root.cityCoord.delete(0, END)
        root.tempEntry.delete(0, END)
        root.humidityEntry.delete(0, END)
        root.windEntry.delete(0, END)
        root.pressureEntry.delete(0, END)
        root.descEntry.delete(0, END)

        # Showing the new results in the tkinter window
        root.cityCoord.insert('0',"LATITUDE : "+latitude+" LONGITUDE : "+longitude)
        root.tempEntry.insert('0',temperature+" °C")
        root.humidityEntry.insert('0',str(humidiy) +" %")
        root.windEntry.insert('0',"SPEED : " +windSpeed+" meter/sec " +
                              " DIRECTION : "+windDirect+"°")
        root.pressureEntry.insert('0',pressure+" hPa")
        root.descEntry.insert('0',weatherDescription)
    # If cod key value is 404 then city is not found
    else:
        messagebox.showerror("ERROR", "CITY NOT FOUND!")

# Defining clearEntries() to clear the values from the text entries of tkinter window
def clearEntries():
    cityName.set('')
    root.cityCoord.delete(0, END)
    root.tempEntry.delete(0, END)
    root.humidityEntry.delete(0, END)
    root.windEntry.delete(0, END)
    root.pressureEntry.delete(0, END)
    root.descEntry.delete(0, END)

# Creating object of tk class
root = tk.Tk()
# Setting the title, background color, windowsize & disabling the resizing property
root.title("PyWeatherDetector")
root.config(background="darkslategray4")
root.geometry("570x320")
root.resizable(False, False)
# Creating tkinter variable
cityName = StringVar()
# Calling the CreateWidgets() function
CreateWidgets()
# Defining infinite loop to run application
root.mainloop()
