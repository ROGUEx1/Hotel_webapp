import pandas as pd

control = ["manage", "cater", "maintain", "house"]
ctrl_p = "admin"


def food_admin():
    a = pd.read_csv("static/databases/food.csv")
    a.to_html("templates/food_panel.html")
    html_file = a.to_html()
    return html_file


def manage_admin():
    a = pd.read_csv("static/databases/manage.csv")
    a.to_html("templates/manage_panel.html")
    html_file = a.to_html()
    return html_file


def fix_admin():
    a = pd.read_csv("static/databases/fix.csv")
    a.to_html("templates/fix_panel.html")
    html_file = a.to_html()
    return html_file


def house_admin():
    a = pd.read_csv("static/databases/house.csv")
    a.to_html("templates/house_panel.html")
    html_file = a.to_html()
    return html_file


def manage_send(room, email, subject, context):
    start = open("static/databases/manage.csv", "a")
    feed = [str(room), ',', str(email), ',', str(subject), ',', str(context), '\n']
    print("\nRoom: ", room, "\nEmail: ", email, "\nSubject: ", subject, "\nContext: ", context)
    start.writelines(feed)
    start.close()
    print("\nDone and Closed!\n")


def house_keeping(room, email, subject, context):
    start = open("static/databases/house.csv", "a")
    feed = [str(room), ',', str(email), ',', str(subject), ',', str(context), '\n']
    print("\nRoom: ", room, "\nEmail: ", email, "\nSubject: ", subject, "\nContext: ", context)
    start.writelines(feed)
    start.close()
    print("\nDone and Closed!\n")


def fix_main(room, email, subject, context):
    start = open("static/databases/fix.csv", "a")
    feed = [str(room), ',', str(email), ',', str(subject), ',', str(context), '\n']
    print("\nRoom: ", room, "\nEmail: ", email, "\nSubject: ", subject, "\nContext: ", context)
    start.writelines(feed)
    start.close()
    print("\nDone and Closed!\n")


def food_order(room_id, starters, main_course, drinks, dessert, lunch, dinner, deliver):
    start = open("static/databases/food.csv", "a")
    feed = ['\n', str(room_id), ',', str(starters), ',', str(main_course), ',', str(drinks),
            str(dessert), ',', str(lunch), ',', str(dinner), ',', str(deliver)]
    print("\nRoom id: ", room_id, "\nStarters: ", starters, "\nMain course: ", main_course, "\nDrinks: ", drinks,
          "\nDessert: ", dessert, "\nLunch: ", lunch, "\nDinner: ", dinner, "\nDeliver to: ", deliver, "\n")
    start.writelines(feed)
    start.close()
    print("\nDone and Closed!\n")
