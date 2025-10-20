from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "6144b668dd5f8fbf1b85bccf1d92a2ca"

def get_weather_data(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

@app.route("/weather", methods=["GET"])
def weather():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "City parameter is required"}), 400

    data = get_weather_data(city)
    if not data or data.get("cod") != 200:
        return jsonify({"error": "Could not retrieve weather data"}), 500

    # Simplify the JSON for easier frontend use
    return jsonify({
        "city": data["name"],
        "country": data["sys"]["country"],
        "temp": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "description": data["weather"][0]["description"].capitalize(),
    })

if __name__ == "__main__":
    app.run(debug=True)