from flask import Flask, render_template, request, jsonify
from scripts.api_utils import fetch_weather, fetch_alerts

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.json['city']
    weather, temp = fetch_weather(city)
    return jsonify({"weather": weather, "temp": temp})

@app.route('/alerts', methods=['POST'])
def alerts():
    lat = request.json['lat']
    lon = request.json['lon']
    alerts = fetch_alerts(lat, lon)
    return jsonify(alerts)

if __name__ == "__main__":
    app.run(debug=True)
