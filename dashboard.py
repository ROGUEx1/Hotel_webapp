from flask import Flask, render_template, request, redirect
import os
import pandas as pd
from admin import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template("login.html")


data = []


@app.route('/login', methods=['GET', 'POST'])
@app.route('/register', methods=['GET', 'POST'])
def check_in():
    room_new = request.form["room_new"]
    passkey = request.form["pass"]
    print("\nSignup room: ", room_new, "\nSignup password: ", passkey, "\n")
    data.append(room_new)
    data.append(passkey)
    return render_template("login.html")


@app.route('/service', methods=['GET', 'POST'])
def service():
    room = request.form["room_id"]
    password = request.form["password"]
    print("\nLogin room: ", room, "\nLogin password: ", password, "\n")
    print(data, '\n')
    control = ["manage", "cater", "maintain", "serve"]
    ctrl_key = "admin"
    if room in control and password == ctrl_key:
        employee()
        return render_template("employee.html")
    elif (room not in data) and (password not in data):
        return render_template("login.html")
    else:
        return render_template("service.html")


if __name__ == '__main__':
    app.run(debug=True, port=5001)
