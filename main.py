from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

city_name = requests.get("https://ipinfo.io/").json()
data = requests.get(
    f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city_name["city"]}').json()


def to_celcius(temp):
    return temp - 273.15


def to_fahrenite(temp):
    return (temp - 273.15) * 9/5 + 32


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html", weatherData=data, convertToCelecius=to_celcius, convertToFahrenite=to_fahrenite, cityName=city_name["city"])


if __name__ == "__main__":
    app.run(debug=True)
