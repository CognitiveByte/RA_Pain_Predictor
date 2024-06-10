import os
from flask import Flask, request, jsonify, render_template
import requests
import numpy as np
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

def predict_pain_level(temperature, humidity, pressure):
    # Using coefficients derived from studies
    temp_effect = -0.16 * (temperature - 20)  # Example coefficient for temperature
    humidity_effect = 0.15 * (humidity - 50)  # Example coefficient for humidity
    pressure_effect = -0.10 * (pressure - 1015)  # Example coefficient for pressure
    
    # Simple linear combination of effects
    pain_level = 5 + temp_effect + humidity_effect + pressure_effect
    pain_level = np.clip(pain_level, 0, 10)  # Ensure pain level is between 0 and 10
    return pain_level

def fetch_weather(location):
    api_key = os.getenv("WEATHER_API_KEY")
    url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={location}&days=3"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Python 3.6+
    except requests.exceptions.RequestException as req_err:
        print(f"Error occurred: {req_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    location = data['location']
    weather_data = fetch_weather(location)

    if not weather_data:
        return jsonify({
            'error': 'Could not fetch weather data. Please try again later.'
        })

    current_conditions = weather_data['current']
    temperature = current_conditions['temp_c']
    humidity = current_conditions['humidity']
    pressure = current_conditions['pressure_mb']

    pain_level = predict_pain_level(temperature, humidity, pressure)

    return jsonify({
        'location': location,
        'current_conditions': current_conditions,
        'pain_level_prediction': round(pain_level, 1)
    })

if __name__ == '__main__':
    app.run(debug=True)
