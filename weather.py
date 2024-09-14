import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

load_dotenv()
api_key = os.getenv('API_KEY')

@dataclass
class WeatherData:
    """Class to handle the weather data"""
    main: str
    description: str
    icon: str
    current: float

def get_loc(city_name, country_code, API_key):
    """Get the location of the city using geocoding API"""
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_code}&appid={API_key}').json()
    data = response[0]
    lat, lon = data.get('lat'), data.get('lon')

    return lat, lon

def current_weather(lat, lon, API_key):
    """Fetch the current weather data"""
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric').json()
    data = WeatherData(
        main = response.get('weather')[0].get('main'),
        description = response.get('weather')[0].get('description'),
        icon = response.get('weather')[0].get('icon'),
        current = response.get('main').get('temp')
    )
    return data

def next_three_days_weather(lat, lon, API_key):
    """Fetch the weather for the next 3 days (including today)"""
    response = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_key}&units=metric').json()
    forecast = response.get('list', [])
    
    daily_forecast = {}

    for entry in forecast:
        date = entry['dt_txt'].split(' ')[0]
        temp_max = entry['main'].get('temp_max')
        temp_min = entry['main'].get('temp_min')

        if date not in daily_forecast:
            daily_forecast[date] = {'high_temp': temp_max, 'low_temp': temp_min}
        else:
            daily_forecast[date]['high_temp'] = max(daily_forecast[date]['high_temp'], temp_max)
            daily_forecast[date]['low_temp'] = min(daily_forecast[date]['low_temp'], temp_min)

    result = []
    for i, (date, temps) in enumerate(daily_forecast.items()):
        if i < 4:
            result.append({
                'date': date,
                'high_temp': temps['high_temp'],
                'low_temp': temps['low_temp'],
            })

    return result

def main(city_name, country_name):
    lat, lon = get_loc(city_name, country_name, api_key)
    current_data = current_weather(lat, lon, api_key)
    today_data = next_three_days_weather(lat, lon, api_key)[0]
    next_three_days = next_three_days_weather(lat, lon, api_key) [1:4]
    return {
        "current_weather": current_data,
        "today_forecast": today_data,
        "next_three_days": next_three_days
    }

if __name__ == "__main__":
    pass
