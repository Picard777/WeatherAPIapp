Weather CLI App (Python)

A simple command-line weather application written in Python that retrieves current weather data for a city using the OpenWeatherMap API. 
Project idea from: https://roadmap.sh/projects/weather-api-wrapper-service

The app:
Converts a city name into geographic coordinates (latitude & longitude)
Fetches real-time weather data
Displays temperature, feels-like temperature, and weather conditions

Features:
1.City-based weather lookup
2.Uses OpenWeatherMap Geocoding API
3.Displays temperature in Celsius
4.Shows weather condition description
5.Simple CLI interface (easy to extend)

Technologies Used:
-Python 3
-requests library
-OpenWeatherMap API

Requirements:
Make sure u have Python installed, then install dependencies:
pip install requests

API Key Setup:
This project uses the OpenWeatherMap API.

Create a free account at:
https://openweathermap.org/api

Generate an API key.
Replace the API key in the script:
API_KEY = "YOUR_API_KEY_HERE"
Important: Do not expose your API key in public repositories.

How to Run:
1.Clone or download the project
2.Open a terminal in the project folder
3.Run:
python weather.py
4.Enter a city name when prompted:
5.Enter a city: London

Sample Output:
Location:
Country: GB
Latitude: 51.5074
Longitude: -0.1278

Weather:
Temperature: 18°C
Feels like: 17°C
Condition: Light Rain

Notes & Limitations:
Uses the current weather endpoint only
Internet connection required
City name ambiguity may return the first matching result

Possible Improvements:
Add forecast support
Support state/country input
Error handling for API failures
Environment variable for API key
GUI or web interface

