import requests

#Change these variables to match your location
latitude = 
longitude =

#API information request + variable setting
response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max,temperature_2m_min&current_weather=true&timezone=auto&forecast_days=1").json()
currentTemp = response["current_weather"]["temperature"]
weatherCode = response["current_weather"]["weathercode"]
maxTemp = response["daily"]["temperature_2m_max"]
minTemp = response["daily"]["temperature_2m_min"]


# Put this in a separate file
weatherCodeIDs = {
    0:"Clear sky",
    1:"Clear", 2:"Partly cloudy", 3:"Overcast",
    45:"Fog", 48:"Fog",
    51:"Drizzle", 53:"Drizzle", 55:"Drizzle", 56: "Freezing drizzle", 57:"Freezing drizzle",
    61:"Slight rain", 63:"Moderate rain", 65:"Heavy rain",
    66:"Freezing rain", 67:"Freezing rain",
    71:"Light snow fall", 73:"Moderate snow fall", 75:"Heavy snow fall", 77:"Snow",
    80:"Light showers", 81:"Moderate showers", 82:"Violent showers",
    85:"Light snow showers", 86:"Heavy snow showers",
    95:"Thunderstorm", 96:"Thunderstorm + Light hail", 99:"Thunderstorm + Heavy hail"
}

print(weatherCodeIDs[weatherCode])