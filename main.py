import json
from urllib.request import urlopen

"""create a program that looks at the api of a weather channel and return the current weather of your
city: Ottawa, Montreal, and Toronto, in json format. Then the program should execute once every hour 
"""
with urlopen('https://api.openweathermap.org/data/2.5/weather?lat=45.4208777&lon=-75.6901106&appid=02f1340c52d03e246c293f1747c33322')as source:
    data = source.read()
    new_data = json.loads(data)
# print(new_data)
currentTemp = new_data['main']['temp']-273.15
feels_like = new_data['main']['feels_like']-273.15
windSpeed = new_data['wind']['speed']
print()
print("Current weather in Ottawa, ON")
print()
print("Current temperature is: ", end="")
print("%.2f "%currentTemp+"Celsius")
print("Real feel is:", end="")
print("%.2f "%feels_like+"Celsius")
print(f"Location is: {new_data['name']}, "+f"{new_data['sys']['country']}")
print(f"Wind speed is: {windSpeed} Km/h")

print(__doc__)
# for item in new_data:
#     print(item)
