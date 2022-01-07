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


@app.route('/')
@app.route('/home')
@app.route('/login')
def home():
    return render_template("login.html")


temp = {"room_id": "123", "password": "password"}


@app.route('/service', methods=['GET', 'POST'])
def service():
    room = request.form["room_id"]
    password = request.form["password"]
    print(room, password)
    if room not in temp:
        return render_template("login.html")
    elif temp[room] != password:
        return render_template("login.html")
    else:
        return render_template("service.html")




if __name__ == '__main__':
    app.run(debug=True, port=5001)
