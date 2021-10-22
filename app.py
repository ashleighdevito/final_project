#T.Bradford
#October 2021

#Dependencies
import pandas as pd
import sqlalchemy
from flask import Flask, json, request, jsonify, render_template, redirect
import decimal
from sqlalchemy import create_engine, inspect, func
from importlib import reload
import pickle 
#from upcoming_data import dune, ron, souvenir, spencer, mothering_sunday, humans, rocket, song
import numpy as np

dune = [[155,75.0,8.4,21000000,4,1,0,0.0,0,1,0.0,0.0,0.0,0,1,0.0,0.0,0.0,0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,10,0.0,0.0,0.0,0,1,0,0.0,0.0,0.0,0.0]]
ron = [[106,68.0,6.3,21000000,4,1,1,0.0,1,0,0.0,0.0,0.0,0,0,0.0,0.0,0.0,0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,10,0.0,0.0,0.0,1,0,0,0.0,0.0,0.0,0.0]]
souvenir = [[106,98.0,8.0,21000000,4,0,0,0.0,0,0,0.0,0.0,0.0,0,1,0.0,0.0,0.0,0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,10,0.0,0.0,0.0,0,0,1,0.0,0.0,0.0,0.0]]
spencer = [[111,85.0,6.4,21000000,4,0,0,0.0,0,0,0.0,0.0,0.0,1,1,0.0,0.0,0.0,1,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,11,0.0,0.0,0.0,0,0,1,0.0,0.0,0.0,0.0]]
mothering_sunday = [[110,69.0,6.2,21000000,4,0,0,0.0,0,0,0.0,0.0,0.0,0,1,0.0,0.0,0.0,0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,11,0.0,0.0,0.0,0,0,1,0.0,0.0,0.0,0.0]]
humans = [[108,78.0,7.3,21000000,4,0,0,0.0,0,0,0.0,0.0,0.0,0,1,0.0,0.0,0.0,0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,11,0.0,0.0,0.0,0,0,1,0.0,0.0,0.0,0.0]]
rocket =[[128,78.0,7.0,21000000,4,0,1,0.0,0,0,0.0,0.0,0.0,0,1,0.0,0.0,0.0,0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,12,0.0,0.0,0.0,0,0,1,0.0,0.0,0.0,0.0]]
song = [[105,66.0,7.0,21000000,4,0,0,0.0,0,0,0.0,0.0,0.0,0,1,0.0,0.0,0.0,0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,8,0.0,0.0,0.0,0,0,1,0.0,0.0,0.0,0.0]]

model = pickle.load(open("rf_model.pkl", "rb"))

# Create an instance of our Flask app.
app = Flask(__name__)

@app.route("/")
def home():

    # Return template and data
    return render_template("index.html", prediction_text = "Run the model to see a box office prediction.")


@app.route("/index")
def index():

    # Return template and data
    return render_template("index.html", prediction_text = "Run the model to see a box office prediction.")
# Set route
@app.route("/team")
def team():

    # Return template and data
    return render_template("team.html")
    
@app.route("/model")
def model_page():

    # Return template and data
    return render_template("model.html")

# Set route
@app.route("/predict-dune")
def predict_dune():
    #float_features = [float(x) for x in request.form.values()]
    # float_features = [128,53,5.6,400000,6,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,0,0,0,1,0,0,0,0,0,0]
    # features = [np.array(float_features)]
    
    prediction = model.predict(dune)
    return render_template("index.html", prediction_text = "Dune has a boxoffice prediction of {}".format(prediction))

@app.route("/predict-ron")
def predict_ron():
    
    prediction = model.predict(ron)
    return render_template("index.html", prediction_text = "Ron's Gone Wrong has a boxoffice prediction of {}".format(prediction))

@app.route("/predict-souvenir")
def predict_souvenir():
    
    prediction = model.predict(souvenir)
    return render_template("index.html", prediction_text = "The Souvenir: Part II has a boxoffice prediction of {}".format(prediction))

@app.route("/predict-spencer")
def predict_spencer():
    
    prediction = model.predict(spencer)
    return render_template("index.html", prediction_text = "Spencer has a boxoffice prediction of {}".format(prediction))

@app.route("/predict-mothering_sunday")
def predict_mothering():
    
    prediction = model.predict(mothering_sunday)
    return render_template("index.html", prediction_text = "Mothering Sunday has a boxoffice prediction of {}".format(prediction))

@app.route("/predict-humans")
def predict_humans():
    
    prediction = model.predict(humans)
    return render_template("index.html", prediction_text = "The Humans has a boxoffice prediction of {}".format(prediction))

@app.route("/predict-rocket")
def predict_rocket():
    
    prediction = model.predict(rocket)
    return render_template("index.html", prediction_text = "Red Rocket has a boxoffice prediction of {}".format(prediction))

@app.route("/predict-song")
def predict_song():
    
    prediction = model.predict(song)
    return render_template("index.html", prediction_text = "Swan Song has a boxoffice prediction of {}".format(prediction))

if __name__ == '__main__':
    app.jinja_env.cache = {}
    app.run(debug=True, threaded=True)