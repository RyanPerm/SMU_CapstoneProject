from flask import Flask, render_template, jsonify, send_from_directory, request
import json
import pandas as pd
import numpy as np
import os
from modelHelper import ModelHelper

#init app and class
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
modelHelper = ModelHelper()

#endpoint
# Favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')

# Route to render index.html template
@app.route("/")
def home():
    # Return template and data
    return render_template("index.html")

@app.route("/makePredictions") # methods=["POST"]
def makePredictions():

    # dummy data

    distance = .1
    temperature = 52.0
    humidity = 35.0
    wind_speed = 8.2
    pressure = 21.00
    road_type = "Highway"
    visibility = 1.0
    side = "Left"
    condition = "Thunderstorm"





    # content = request.json["data"]

    # # parse
    # condition = int(content["condition"])
    # temperature = float(content["temperature"])
    # wind_speed = float(content["wind_speed"])
    # humidity = int(content["humidity"])
    # pressure = int(content["pressure"])
    # road_type = content["type"]
    # side = content["side"]

    prediction = modelHelper.makePredictions(distance, visibility, side, condition, temperature, wind_speed, humidity, pressure, road_type)
    print(prediction)
    return(jsonify({"ok": True, "prediction": str(prediction)}))

####################################
# ADD MORE ENDPOINTS

###########################################

#############################################################

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

#main
if __name__ == "__main__":
    app.run(debug=True)