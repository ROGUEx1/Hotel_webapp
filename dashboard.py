# import cgi
# import webbrowser
#
# webbrowser.open_new_tab('http://localhost:63342/Hotel_webapp/Static/login.html')
#
# form = cgi.FieldStorage()
#
# room = form.getvalue("room_id")
#
# print(room)

from flask import Flask, render_template, request, redirect
import os

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
    print(room_new, passkey)
    data.append(room_new)
    data.append(passkey)
    return render_template("login.html")


@app.route('/service', methods=['GET', 'POST'])
def service():
    room = request.form["room_id"]
    password = request.form["password"]
    print(room, password)
    if (room not in data) and (password not in data):
        return render_template("login.html")
    else:
        return render_template("service.html")


if __name__ == '__main__':
    app.run(debug=True, port=5001)
