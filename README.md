# Weather API App

A Python-based weather application that retrieves real-time weather information using Open-Meteo APIs.

## Features

* Search weather by city name
* Automatic latitude and longitude lookup
* Displays current temperature
* Displays current humidity
* Displays maximum temperature of the day
* Displays minimum temperature of the day
* Handles invalid city names
* Handles empty input
* Basic API error handling

## Technologies Used

* Python
* Requests Library
* Open-Meteo Geocoding API
* Open-Meteo Weather API

## How It Works

1. User enters a city name.
2. The Geocoding API retrieves the city's latitude and longitude.
3. The Weather API fetches weather information for that location.
4. The application displays:

   * Current temperature
   * Current humidity
   * Daily maximum temperature
   * Daily minimum temperature

## Installation

Install the required library:

```bash
pip install requests
```

## Run

```bash
python weather_api.py
```
