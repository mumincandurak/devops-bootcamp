import os
import requests
from dotenv import load_dotenv

load_dotenv()

def weather_request(url):
    try:
        weather = requests.get(url, timeout=10)  # Set a timeout for the request
        weather.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
        return weather.json()  # Assuming the API returns JSON data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

api_key = os.getenv("WEATHER_API_KEY")
url = f"https://api.openweathermap.org/data/2.5/weather?lat=37.966461&lon=34.662479&lang=tr&units=metric&appid={api_key}"
data = weather_request(url)

if data:
    print(f"Weather is for the {data['name']} is {data['main']['temp']}°C and status is {data['weather'][0]['description']}.")