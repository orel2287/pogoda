import requests
from flask import Flask, render_template, request, jsonify

API_KEY = '47d89e1c6e7a4d908f47327c49d7bfeb'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=' + API_KEY

app = Flask(__name__)

def get_weather(city):
    url = BASE_URL.format(city=city)
    response = requests.get(url)
    data = response.json()

    # Форматируем данные для вывода
    weather_info = {
        'city': city,
        'temperature': round(data['main']['temp'] - 273.15, 2),  # Перевод в Цельсий
        'description': data['weather'][0]['description'],
        'humidity': data['main']['humidity'],
        'pressure': data['main']['pressure'],
        'wind_speed': data['wind']['speed'],
        'icon': f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png"
    }

    return weather_info

@app.route('/weather/<city>')
def weather(city):
    weather_data = get_weather(city)
    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True)
