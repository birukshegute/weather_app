import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass
from datetime import datetime, timedelta

load_dotenv()
api_key = os.getenv('API_KEY')

@dataclass
class WeatherData:
    """Class to handle the weather data"""
    main: str
    description: str
    icon: str
    current: float
    max: float
    min: float

def get_loc(city_name, country_code, API_key):
    """Get the location of the city using geeocoding api"""
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_code}&appid={API_key}').json()
    data = response[0]
    lat, lon = data.get('lat'), data.get('lon')

    return lat, lon

def current_weather(lat, lon, API_key):
    """fetch the weather data for today"""
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric').json()
    data = WeatherData(
        main = response.get('weather')[0].get('main'),
        description = response.get('weather')[0].get('description'),
        icon = response.get('weather')[0].get('icon'),
        current = response.get('main').get('temp'),
        max = response.get('main').get('temp_max'),
        min = response.get('main').get('temp_min'),
    )
    return data

def next_three_days_weather(lat, lon, API_key):
    """Fetch the weather for the next 3 days"""
    response = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_key}&units=metric').json()
    forecast = response.get('list', [])
    
    daily_forecast = []

    for i in range(0, 24, 8):
        day = forecast[i]
        daily_forecast.append({
            'date': day.get('dt_txt'),
            'high_temp': day.get('main').get('temp_max'),
            'low_temp': day.get('main').get('temp_min'),
            'description': day.get('weather')[0].get('description')
        })
    
    return daily_forecast

def last_three_days_weather(lat, lon, API_key):
    """Fetch the weather for the last 3 days."""
    end_time = int(datetime.now().timestamp())
    start_time = int((datetime.now() - timedelta(days=3)).timestamp())
    
    url = f'https://history.openweathermap.org/data/2.5/history/city?lat={lat}&lon={lon}&type=hour&start={start_time}&end={end_time}&appid={API_key}&units=metric'
    
    response = requests.get(url).json()
    history_data = response.get('list', [])
    
    daily_history = []
    
    for i in range(0, len(history_data), 8):
        day = history_data[i]
        daily_history.append({
            'date': datetime.utcfromtimestamp(day.get('dt')).strftime('%Y-%m-%d'),
            'high_temp': day.get('main').get('temp_max'),
            'low_temp': day.get('main').get('temp_min'),
            'description': day.get('weather')[0].get('description'),
        })
    
    return daily_history

def main(city_name, country_name):
    lat, lon = get_loc('Addis Ababa', 'Ethiopia', api_key)
    current_data = current_weather(lat, lon, api_key)
    next_three_days = next_three_days_weather(lat, lon, api_key)
    last_three_days = last_three_days_weather(lat, lon, api_key)
    return {
        "current_weather": current_data,
        "next_three_days": next_three_days,
        "last_three_days": last_three_days
    }

if __name__ == "__main__":
    pass