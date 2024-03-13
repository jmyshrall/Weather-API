# Weather Forecast Program

This Python program fetches weather forecast data from the OpenWeatherMap API, caches it locally, and displays the forecast to the user. It also supports running in offline mode by utilizing cached data when an internet connection is unavailable.

## Features

- Fetches weather forecast data from the OpenWeatherMap API based on user input (city/zip code, preferred units, forecast days).
- Caches fetched data locally to reduce API requests and provide offline functionality.
- Displays weather forecast including date, temperature, and description for each forecasted period.
- Runs in offline mode when unable to fetch data from the API, using cached data if available.

## Dependencies

- Python 3.x
- `requests` library (install via `pip install requests`)

## Usage

1. Clone the repository or download the `weather_forecast.py` file.
2. Ensure you have a valid API key from OpenWeatherMap. Place the API key in a file named `config.py` with a function `get_api_key()` that returns the API key as a string.
3. Run the program by executing the `weather_forecast.py` file:

python weather_forecast.py

4. Follow the prompts to input the city/zip code, preferred units (Fahrenheit, Celsius, Kelvin), and number of forecast days (1-7).
5. View the weather forecast displayed in the console.

## Example

Enter the name of the city/zip code: New York
Enter preferred units (F/C/K): C
Enter number of forecast days (1-7): 3

Date: 2024-03-13 00:00:00, Temperature: 5.2°C, Description: broken clouds
Date: 2024-03-13 03:00:00, Temperature: 4.8°C, Description: broken clouds
Date: 2024-03-13 06:00:00, Temperature: 4.5°C, Description: scattered clouds
...

## Notes

- Ensure your API key is kept confidential and not shared publicly to prevent unauthorized use.
- Cached data is stored in a file named `weather_cache.json` in the same directory as the program.

Feel free to modify and extend the program according to your needs!