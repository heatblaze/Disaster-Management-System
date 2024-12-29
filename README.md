# Disaster-Management-System

A web and desktop-based disaster management system that provides weather updates and disaster alerts using APIs. The system offers a Google Maps integration to visualize disaster-prone areas and features a Tkinter GUI for desktop users.

---

## Features
**Web Application**:
- **Weather Updates:** Get real-time weather conditions and temperature by entering a city name.
- **Disaster Alerts:** Fetch alerts based on latitude and longitude coordinates.
- **Google Maps Integration:** Displays disaster-prone areas on a map.
**Desktop Application**
- **Tkinter GUI:** Fetch weather and alerts through an easy-to-use graphical interface.

## Tech Stack
**Backend:** *Flask*
**Frontend:** *HTML, JavaScript, Tkinter*
**APIs Used:**
- *OpenWeatherMap API for weather data and alerts*
- *Google Maps API for map rendering*
- *Database: None (API-driven system)*

## Prerequisites
- Python 3.7 or higher
- Required Python libraries: Flask, requests, tkinter
- OpenWeatherMap API key
- Google Maps API key

---

## Usage

**Web Application**
1. Open the web application in your browser.
2. Use the weather form to fetch current weather details for a city.
3. Visualize disaster-prone areas on the embedded Google Map.
   
**Desktop Application**
1. Enter a city name to fetch weather details.
2. Enter latitude and longitude coordinates to fetch disaster alerts.

---

## API Details
**OpenWeatherMap API**
Endpoints:
- Weather Data: http://api.openweathermap.org/data/2.5/weather
- Alerts Data: https://api.openweathermap.org/data/3.0/onecall

**Google Maps API**
Embedded in the web application for disaster-prone area visualization.

---

## Notes
- API keys should be stored securely and not shared publicly.
- Ensure proper handling of rate limits for the OpenWeatherMap and Google Maps APIs.
- There are some issues with packages in the main file which needs fixing as well.

---

## Contributing
1. Fork the repository.
2. Create a feature branch (git checkout -b feature-name).
3. Commit your changes.
4. Push to the branch (git push origin feature-name).
5. Open a pull request.

---

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/heatblaze/Disaster-Management-System.git
