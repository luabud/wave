from flask import render_template
from datetime import datetime
from . import app
from . import wave

@app.route("/")
def home():
    numspaces_list = []
    for i in range(0, 1800, 3):
        numspaces_list.append(wave.make_dot(i))
return render_template("home.html",numspaces_list=(numspaces_list))

