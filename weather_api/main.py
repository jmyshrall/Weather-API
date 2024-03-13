"""
Author: Justin Myshrall
Date: 3/13/2024
"""

import config
import requests
import json
from datetime import datetime, timedelta

# File to store cached weather data
CACHE_FILE = 'weather_cache.json'

def get_forecast(api_key, city, units='metric', days=3):
    # Check if cached data is available and valid
    cached_data = load_cache()
    if cached_data:
        if 'forecast' in cached_data and cached_data['city'] == city:
            forecast_data = cached_data['forecast']
            if is_cache_valid(forecast_data):
                # Use cached data if it's still valid
                print("Fetching data from cache...")
                print_weather_forecast(forecast_data)
                return

    # Fetch data from the API if cache is not valid or not available
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units={units}&cnt={days}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Save fetched data to cache
        save_cache(data, city)
        print_weather_forecast(data)
    else:
        # If fetching data from the API fails, run in offline mode
        print('Error fetching forecast data. Running in offline mode...')
        # Check if there's cached data available to display
        if cached_data and 'forecast' in cached_data:
            print_weather_forecast(cached_data['forecast'])
        else:
            print('No cached data available.')

def save_cache(data, city):
    # Save data to cache file along with city name and timestamp
    cached_data = {
        'city': city,
        'forecast': data,
        'timestamp': datetime.now().timestamp()
    }
    with open(CACHE_FILE, 'w') as cache_file:
        json.dump(cached_data, cache_file)

def load_cache():
    try:
        # Load cached data from file
        with open(CACHE_FILE, 'r') as cache_file:
            return json.load(cache_file)
    except FileNotFoundError:
        # Return None if cache file doesn't exist
        return None

def is_cache_valid(data):
    if 'timestamp' in data:
        # Check if cached data is less than 1 hour old
        timestamp = data['timestamp']
        if datetime.now() - datetime.fromtimestamp(timestamp) < timedelta(hours=1):
            return True
    return False

def print_weather_forecast(data):
    # Print weather forecast for each data point
    for forecast in data['list']:
        date = forecast['dt_txt']
        temp = forecast['main']['temp']
        desc = forecast['weather'][0]['description']
        print(f'Date: {date}, Temperature: {temp}°C, Description: {desc}')

def main():
    city = input('Enter the name of the city/zip code: ')
    units = input('Enter preferred units (F/C/K): ').lower()
    days = int(input('Enter number of forecast days (1-7): '))

    if units not in ['f', 'c', 'k'] or not 1 <= days <= 7:
        # Validate user input for units and forecast days
        print('Invalid input. Please enter F, C, or K for units and a number between 1 and 7 for forecast days.')
        return

    units_mapping = {'f': 'imperial', 'c': 'metric', 'k': 'standard'}
    api_units = units_mapping[units]

    api_key = config.get_api_key()

    # Call get_forecast function to fetch and display weather forecast
    get_forecast(api_key, city, api_units, days)

if __name__ == "__main__":
    main()