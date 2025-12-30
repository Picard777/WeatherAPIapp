import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("WEATHER_API_KEY")
ONECALL_URL = "https://api.openweathermap.org/data/2.5/weather"
GEO_URL = "http://api.openweathermap.org/geo/1.0/direct"

def get_coordinates(city, limit=1):
    params = {
        'q': city,
        'appid': api_key,
        'limit': 1
    }
    response = requests.get(GEO_URL, params=params).json()
    if not response:
        return None
    
    if isinstance(response, dict):
        print("Geocoding API error:", response)
        return None

    if not response:
        return None

    return response[0]["lat"], response[0]["lon"]

def get_weather(lat, lon):
    params = {
        'lat': lat,
        'lon': lon,
        'appid': api_key,
        'units': "metric",
    }
    
    return requests.get(ONECALL_URL, params=params).json()

def show_weather(data, lat, lon, country):
    if 'main' in data:
        
        country = data["sys"].get("country", "Unknown")
        print("\nLocation:")
        print(f"Country: {country}")
        print(f'Latitude: {lat}')
        print(f'Longitude: {lon}')
        
        
        print("\nWeather:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Feelks like: {data['main']['feels_like']}°C")
        print(f"Condition {data['weather'][0]['description'].title()}")
    else:
        print("\nErrro:", data.get("message, 'Unable to retrieve weather"))
    
def main():
    city = input("Enter a city: ")
    coords = get_coordinates(city)
    if coords is None:
        print("City not found!")
        return
    
    lat, lon = coords
    weather_data = get_weather(lat, lon)
    show_weather(weather_data, lat, lon, country="")
    if main() == True:
        return main()
if __name__ == '__main__':
    main()
    