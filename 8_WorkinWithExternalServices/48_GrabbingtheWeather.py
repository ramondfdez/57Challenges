# Using the OpenWeatherMap API at http://openweathermap.org/
# current, create a program that prompts for a city name and
# returns the current temperature for the city.
# 
# Example Output
# Where are you? Chicago IL
# Chicago weather:
# 65 degrees Fahrenheit
# 
# Constraint
# • Keep the processing of the weather feed separate from
# the part of your program that displays the results.

import requests

city = input("Where are you? ")

response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=0b57c7f7e39e3022114fedd82a4f4a5a")

json = response.json()

temperatura = str(json['main']['temp'])

print (city +  " weather: ")
print (temperatura + " degrees Fahrenheit: ")