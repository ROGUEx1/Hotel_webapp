import pandas as pd


def employee():
    a = pd.read_csv("static/databases/user.csv")
    a.to_html("templates/employee.html")
    html_file = a.to_html()
    return html_file


employee()
