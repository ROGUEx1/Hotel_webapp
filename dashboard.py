import guest
from Sign_up import *
from flask import Flask, render_template, request
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
    room = request.form["room_new"]
    passkey = request.form["pass"]
    print("\nSignup room: ", room, "\nSignup password: ", passkey, "\n")
    new_guest = guest.Guest(room, passkey)
    data.append(new_guest)
    database(new_guest)
    print(data, "\n")
    return render_template("login.html")


@app.route('/service', methods=['GET', 'POST'])
def service():
    room = request.form["room_id"]
    password = request.form["password"]
    print("\nLogin room: ", room, "\nLogin password: ", password, "\n")
    if room in control and password == ctrl_p:
        if room == control[0]:
            manage_admin()
            return render_template("manage_panel.html")
        elif room == control[1]:
            food_admin()
            return render_template("food_panel.html")
        elif room == control[2]:
            fix_admin()
            return render_template("fix_panel.html")
        else:
            house_admin()
            return render_template("house_panel.html")
    else:
        checking = open("static/databases/database.txt", "r")
        room = room + "\n"
        password = password + "\n"
        done = False
        while not done:
            line = checking.readline()
            if line == room:
                auth = checking.readline()
                if password == auth:
                    print("Logging in")
                    done = True
                    return render_template("service.html")
                else:
                    done = True
                    return render_template("login.html")

            if line == "":
                done = True
                return render_template("login.html")


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
    food_order(room_id, starters, main_course, drinks, dessert, lunch, dinner, deliver)
    return render_template('reservation.html')


@app.route('/maintain')
def maintain():
    return render_template('maintain.html')


@app.route('/main_req', methods=['GET', 'POST'])
def main_req():
    room = request.form["room"]
    email = request.form["email"]
    subject = request.form["request"]
    context = request.form["message"]
    print(room, '\n', email, '\n', subject, '\n', context, '\n')
    fix_main(room, email, subject, context)
    return render_template('service.html')


@app.route('/house_keep')
def house():
    return render_template('clean.html')


@app.route('/clean', methods=['GET', 'POST'])
def house_req():
    room = request.form["room"]
    email = request.form["email"]
    subject = request.form["request"]
    context = request.form["message"]
    print(room, '\n', email, '\n', subject, '\n', context, '\n')
    house_keeping(room, email, subject, context)
    return render_template('service.html')


@app.route('/management')
def manage():
    return render_template('manage.html')


@app.route('/managing', methods=['GET', 'POST'])
def manage_req():
    room = request.form["room"]
    email = request.form["email"]
    subject = request.form["request"]
    context = request.form["message"]
    print(room, '\n', email, '\n', subject, '\n', context, '\n')
    manage_send(room, email, subject, context)
    return render_template('service.html')


if __name__ == '__main__':
    app.run(debug=True, port=5001)
