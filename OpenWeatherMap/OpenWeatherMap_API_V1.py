import requests
import json

class OpenMapAPI:
    def __init__(self, api_key) -> None:
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather_by_city(self, city_name):
        url = f"{self.base_url}?q={city_name}&appid={self.api_key}"
        try:
            response = requests.get(url)
            data = response.json()
            return data
        except:
            print(f"Error connecting to API Service. Please check network connection.")
            exit()