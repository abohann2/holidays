import os
import requests
from flask import Flask, render_template, request
app = Flask(__name__)

API_KEY = os.environ.get("API_KEY")

@app.route('/', methods=["POST", "GET"])
def hello_world():

    if request.method == "GET":
        response = requests.get(f"https://calendarific.com/api/v2/holidays?api_key={API_KEY}&country=IN&year=2020")
        holidays = response.json()['response']['holidays']

        print(len(holidays))

    return render_template("index.html", holidays=holidays)