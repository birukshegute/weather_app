import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')

def get_loc(city_name, state_code, country_code, API_key):
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}').json()
    data = response[0]
    lat, lon = data.get('lat'), data.get('lon')

    return lat, lon

def current_weather(lat, lon, API_key):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}').json()
    print(response)

if __name__ == "__main__":
    lat, lon = get_loc('Addis Ababa', 'ET', 'Ethiopia', api_key)
    current_weather(lat, lon, api_key)