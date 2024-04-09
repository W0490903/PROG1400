import OpenWeatherMap_API_V1

# Enter API Key.
api_key = "82005d27a116c2880c8f0fcb866998a0"
open_map = OpenWeatherMap_API_V1.OpenMapAPI(api_key)
KELVIN = 273.15

# Prompt user for city.
city_name = input("Please enter city: ")

city_weather = open_map.get_weather_by_city(city_name)

if city_weather['cod'] == 200:
    print(f"Weather in {city_name}")
    print(f"Conditions: {city_weather['weather'][0]['main'].title()}")
    print(f"Temperature: {round(city_weather['main']['temp'] - KELVIN)}°C")
else:
    print(f"Error {city_weather['cod']}: {city_weather['message'].capitalize()}")