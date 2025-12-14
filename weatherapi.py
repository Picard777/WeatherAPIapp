import json
import requests

API_KEY = "REMOVED_API_KEY"
ONECALL_URL = "https://api.openweathermap.org/data/2.5/weather"
GEO_URL = "http://api.openweathermap.org/geo/1.0/direct"

def get_coordinates(city, state="", country="", limit=1):
    query = f"{city}"
    
    if state:
        query += f",{state}"
    if country:
        query += f",{country}"
    params = {
        'q': city,
        'appid': API_KEY,
        'limit': 1
    }
    response = requests.get(GEO_URL, params=params).json()
    if not response:
        return None
    
    lat = response[0]["lat"]
    lon = response[0]["lon"]
    return lat, lon

def get_weather(lat, lon):
    params = {
        'lat': lat,
        'lon': lon,
        'appid': API_KEY,
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
    show_weather(weather_data, lat, lon)
    
if __name__ == '__main__':
    main()
    