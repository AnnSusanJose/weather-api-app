import requests
cityname=input("Enter the city name: ")
if cityname.strip()=="":
    print("City name cannot be empty")
    exit()
# Get city coordinates
city=requests.get( f"https://geocoding-api.open-meteo.com/v1/search?name={cityname}&count=1")
if city.status_code != 200:
    print("Error fetching location data")
    exit()
geodata=city.json()
if "results" not in geodata:
    print("location not found")
    exit()
lat=geodata["results"][0]["latitude"]
lon=geodata["results"][0]["longitude"]
print(f"Latitude: {lat}, Longitude: {lon}")

r=requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m")
if r.status_code != 200:
    print("Error fetching weather data")
    exit()
weather_data=r.json()
times=weather_data["hourly"]["time"]
temp=weather_data["hourly"]["temperature_2m"]
humidity=weather_data["hourly"]["relativehumidity_2m"]
today_temp = temp[:24]
today_times = times[:24]
today_humidity = humidity[:24]
# Display weather report
print("WEATHER REPORT FOR TODAY")
print("City:",cityname)
print(f"Current temperature: {today_temp[0]} °C at time: {today_times[0]}")
print(f"Current humidity: {today_humidity[0]} % at time: {today_times[0]}")
print("Max temperature:",max(today_temp),"°C at time:",today_times[today_temp.index(max(today_temp))])
print("Min temperature:",min(today_temp),"°C at time:",today_times[today_temp.index(min(today_temp))])
