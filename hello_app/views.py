from flask import Flask
from flask import render_template
from datetime import datetime
from . import app
from . import wave

@app.route("/")
def home():
    numspaces_list = []
    for i in range(0, 1800, 10):
        numspaces_list.append(wave.make_dot_string(i))
    return render_template("home.html",numspaces_list=(numspaces_list))

# code below is based on https://code.visualstudio.com/docs/python/tutorial-flask

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")