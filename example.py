#!/usr/bin python3
import requests

API_KEY = "ddd929482aa63c4dbb230c0a5fe1624e"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
city = "Laayoune"
requests_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(requests_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273, 2)
    humidity = round(data["main"]["humidity"], 2)
    print('Weather', weather)
    print("Temperature", temperature)
    print("Humidity", humidity,"%")
else:
    print("An error occured")