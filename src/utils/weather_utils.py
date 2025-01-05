from datetime import date
from src.helpers.fetch.data_fetch import DataFetch
from src.helpers.load_env.load_env import LoadEnv

def get_weather_for_date(latitude: float, longitude: float, start_date: date, end_date: date) -> dict:
    """
    Fetches weather data for a given latitude and longitude between specified start and end dates.

    Args:
        latitude (float): The latitude of the location.
        longitude (float): The longitude of the location.
        start_date (date): The start date for fetching weather data.
        end_date (date): The end date for fetching weather data.
    Returns:
        dict: A dictionary containing the maximum and minimum temperatures and a message.
              If the start date is before 2016-01-01, returns a message indicating no data is available.
              If the request is successful, returns the temperatures and a success message.
              If there is an error fetching the data, returns None for temperatures and an error message.
    """
    if date.fromisoformat(start_date) < date(2016, 1, 1):
        return {
            'temperature_max': None,
            'temperature_min': None,
            'message': 'There is no weather data for movies released before 2016-01-01'
        }

    open_meteo_url = LoadEnv("WEATHER_URL")

    dataFetch = DataFetch(
        url=open_meteo_url.get_value(),
        params={
        'latitude': latitude,
        'longitude': longitude,
        'start_date': start_date,
        'end_date': end_date,
        'daily': 'temperature_2m_max,temperature_2m_min',
        'timezone': 'auto'
    })

    response = dataFetch.get()

    if response and isinstance(response, dict) and 'daily' in response:
        temp_max = response['daily'].get('temperature_2m_max', [None])[0]
        temp_min = response['daily'].get('temperature_2m_min', [None])[0]

        if temp_max is None or temp_min is None:
            return {
                'temperature_max': temp_max,
                'temperature_min': temp_min,
                'message': 'We apologize, but there are no weather records available for the selected date.'
            }

        return {
            'temperature_max': temp_max,
            'temperature_min': temp_min,
            'message': 'Weather data fetched successfully.'
        }
    else:
        return {
            'temperature_max': None,
            'temperature_min': None,
            'message': 'Error fetching weather data.'
        }
