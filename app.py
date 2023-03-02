from flask import Flask, render_template
from datetime import date

app = Flask(__name__)

@app.route("/")
def hello_world():
    today = todays_date()
    return render_template("index.html", the_date = today)

@app.route("/about")
def about_me():
    return render_template("aboutme.html")
    
@app.route("/resume")
def resume():
    return render_template("resume.html")
    
def todays_date():
    today = date.today()
    str_date = today.strftime("%B %d, %Y")
    return "Today's date is " + str_date
