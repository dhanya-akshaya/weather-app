from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "f714fcaedc9148e7aa071539260905"

@app.route('/', methods=['GET', 'POST'])
def home():

    weather_data = None
    error = None

    if request.method == 'POST':

        city = request.form['city']

        url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"

        response = requests.get(url)

        data = response.json()

        print(data)

        if "current" in data:

            weather_data = {
                "city": data["location"]["name"],
                "temperature": data["current"]["temp_c"],
                "weather": data["current"]["condition"]["text"],
                "humidity": data["current"]["humidity"],
                "wind": data["current"]["wind_kph"],
                "icon": data["current"]["condition"]["icon"]
            }

        else:
            error = "City not found"

    return render_template('index.html', weather_data=weather_data, error=error)

if __name__ == '__main__':
    app.run(debug=True)