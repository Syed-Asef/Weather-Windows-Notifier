import requests

#Change these variables to match your location
latitude = 
longitude =

#API information request
response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max,temperature_2m_min&current_weather=true&timezone=auto&forecast_days=1")
