# WeatherPulse – Real-Time Weather Forecast System

## Overview

WeatherPulse is a Python-based real-time weather application that fetches live weather data using REST API integration. The application displays temperature, humidity, and weather conditions dynamically for multiple cities.

## Features

* Real-time weather forecasting
* Multiple city search functionality
* REST API integration using OpenWeather API
* Error handling and HTTP status code validation
* Data visualization using Matplotlib
* CLI-based interactive application

## Technologies Used

* Python
* Requests Library
* REST API
* JSON
* Matplotlib

## How to Run

1. Install required libraries:

```bash
pip install requests matplotlib
```

2. Add your OpenWeather API key in the code:

```python
API_KEY = "YOUR_API_KEY"
```

3. Run the application:

```bash
python weather_app.py
```

## Project Workflow

* User enters city name
* Application sends GET request to OpenWeather API
* API returns weather data in JSON format
* Program processes and displays weather information
* Weather metrics are visualized using charts

## Future Enhancements

* GUI integration using Tkinter
* 5-day weather forecasting
* Weather icons and themes
* Search history functionality

## Author

Yuvraj Singh
