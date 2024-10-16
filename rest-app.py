from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# NWS API Base URL
NWS_BASE_URL = "https://api.weather.gov/points"

def get_weather_data(lat, lon):
    # Step 1: Get the forecast URL from the NWS API
    response = requests.get(f"{NWS_BASE_URL}/{lat},{lon}")
    if response.status_code != 200:
        return None

    data = response.json()
    forecast_url = data['properties']['forecast']

    # Step 2: Get the forecast data
    forecast_response = requests.get(forecast_url)
    if forecast_response.status_code != 200:
        return None

    forecast_data = forecast_response.json()
    return forecast_data

def characterize_temperature(temperature):
    if temperature >= 85:
        return "hot"
    elif temperature <= 50:
        return "cold"
    else:
        return "moderate"

@app.route('/weather', methods=['GET'])
def weather_forecast():
    # Step 3: Get latitude and longitude from request arguments
    lat = request.args.get('lat')
    lon = request.args.get('lon')

    if not lat or not lon:
        return jsonify({"error": "Latitude and longitude are required"}), 400

    # Step 4: Fetch weather data
    forecast_data = get_weather_data(lat, lon)

    if not forecast_data:
        return jsonify({"error": "Unable to retrieve weather data"}), 500

    # Step 5: Extract today's forecast
    today_forecast = forecast_data['properties']['periods'][0]
    short_forecast = today_forecast['shortForecast']
    temperature = today_forecast['temperature']

    # Step 6: Characterize temperature
    temperature_characterization = characterize_temperature(temperature)

    # Step 7: Return the response
    return jsonify({
        "short_forecast": short_forecast,
        "temperature_characterization": temperature_characterization
    })

if __name__ == '__main__':
    app.run(debug=True)