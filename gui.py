from tkinter import *
from scripts.api_utils import fetch_weather, fetch_alerts

def get_weather():
    city = city_entry.get()
    weather, temp = fetch_weather(city)
    if weather and temp:
        result_label.config(text=f"Weather: {weather}\nTemperature: {temp:.2f}°C")
    else:
        result_label.config(text="Error fetching data.")

def get_alerts():
    lat, lon = map(float, lat_lon_entry.get().split(","))
    alerts = fetch_alerts(lat, lon)
    if alerts:
        alert_text = "\n".join([alert['description'] for alert in alerts])
        alert_label.config(text=f"Alerts:\n{alert_text}")
    else:
        alert_label.config(text="No alerts found.")

# Tkinter App
app = Tk()
app.title("Disaster Alert System")

Label(app, text="Enter City:").pack()
city_entry = Entry(app)
city_entry.pack()
Button(app, text="Get Weather", command=get_weather).pack()
result_label = Label(app, text="")
result_label.pack()

Label(app, text="Enter Lat,Lon:").pack()
lat_lon_entry = Entry(app)
lat_lon_entry.pack()
Button(app, text="Get Alerts", command=get_alerts).pack()
alert_label = Label(app, text="")
alert_label.pack()

app.mainloop()
