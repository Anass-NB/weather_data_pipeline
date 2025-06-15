import requests

api_key = "9ab11a8b33b071d78e0dc40b5fde9eff"
url_api  =f"http://api.weatherstack.com/current?access_key={api_key}&query=Casablanca"

def fetch_data():
    print("Fetching Data from the weather API .... ")
    try: 
        res = requests.get(url_api)
        res = res.json()
        return res
    except Exception as e:
        print(e)
        raise
    
def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'Casablanca, Morocco', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'Casablanca', 'country': 'Morocco', 'region': '', 'lat': '33.593', 'lon': '-7.616', 'timezone_id': 'Africa/Casablanca', 'localtime': '2025-06-12 11:47', 'localtime_epoch': 1749728820, 'utc_offset': '1.0'}, 'current': {'observation_time': '10:47 AM', 'temperature': 22, 'weather_code': 116, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0002_sunny_intervals.png'], 'weather_descriptions': ['Partly cloudy'], 'astro': {'sunrise': '06:20 AM', 'sunset': '08:41 PM', 'moonrise': '10:13 PM', 'moonset': '06:51 AM', 'moon_phase': 'Waning Gibbous', 'moon_illumination': 99}, 'air_quality': {'co': '294.15', 'no2': '5.55', 'o3': '80', 'so2': '14.615', 'pm2_5': '19.795', 'pm10': '29.6', 'us-epa-index': '2', 'gb-defra-index': '2'}, 'wind_speed': 18, 'wind_degree': 12, 'wind_dir': 'NNE', 'pressure': 1016, 'precip': 0, 'humidity': 65, 'cloudcover': 75, 'feelslike': 25, 'uv_index': 6, 'visibility': 8, 'is_day': 'yes'}}



