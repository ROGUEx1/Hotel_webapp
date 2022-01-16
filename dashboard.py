from flask import Flask, render_template, request, redirect
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


@app.route('/food')
@app.route('/templates/index.html')
def food():
    return render_template('index.html')


@app.route('/templates/menu.html')
def menu():
    return render_template('menu.html')


@app.route('/templates/about.html')
def about():
    return render_template('about.html')


@app.route('/templates/blog.html')
def blog():
    return render_template('blog.html')


@app.route('/templates/blog-detail.html')
def blog_detail():
    return render_template('blog-detail.html')


@app.route('/templates/contact.html')
def contact():
    return render_template('contact.html')


@app.route('/templates/gallery.html')
def gallery():
    return render_template('gallery.html')


@app.route('/templates/reservation.html')
def reservation():
    return render_template('reservation.html')


@app.route('/return')
def back():
    return render_template('service.html')


@app.route('/order', methods=['GET', 'POST'])
def orders():
    room_id = request.form["room_id"]
    starters = request.form["starters"]
    main_course = request.form["main_course"]
    drinks = request.form["drinks"]
    dessert = request.form["dessert"]
    lunch = request.form["lunch"]
    dinner = request.form["dinner"]
    deliver = request.form["deliver"]
    print("\nRoom id: ", room_id, "\nStarters: ", starters, "\nMain course: ", main_course, "\nDrinks: ", drinks,
          "\nDessert: ", dessert, "\nLunch: ", lunch, "\nDinner: ", dinner, "\nDeliver to: ", deliver, "\n")
    return render_template('reservation.html')


if __name__ == '__main__':
    app.run(debug=True, port=5001)
