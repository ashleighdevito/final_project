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
from upcoming_data import dune, ron, souvenir, spencer, mothering_sunday, humans, rocket, song
import numpy as np


model = pickle.load(open("best_rf_model.pkl", "rb"))

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
    
    diction = str(model.predict(dune))
    chunks = diction.split("'")
    prediction = chunks[1]

    return render_template("index.html", prediction_text = "Dune has a boxoffice prediction of {}.".format(prediction))

@app.route("/predict-ron")
def predict_ron():
    
    diction = str(model.predict(ron))
    chunks = diction.split("'")
    prediction = chunks[1]

    return render_template("index.html", prediction_text = "Ron's Gone Wrong has a boxoffice prediction of {}.".format(prediction))

@app.route("/predict-souvenir")
def predict_souvenir():

    diction = str(model.predict(souvenir))
    chunks = diction.split("'")
    prediction = chunks[1]

    return render_template("index.html", prediction_text = "The Souvenir: Part II has a boxoffice prediction of {}.".format(prediction))

@app.route("/predict-spencer")
def predict_spencer():

    diction = str(model.predict(spencer))
    chunks = diction.split("'")
    prediction = chunks[1]

    return render_template("index.html", prediction_text = "Spencer has a boxoffice prediction of {}.".format(prediction))

@app.route("/predict-mothering_sunday")
def predict_mothering():

    diction = str(model.predict(mothering_sunday))
    chunks = diction.split("'")
    prediction = chunks[1]

    return render_template("index.html", prediction_text = "Mothering Sunday has a boxoffice prediction of {}.".format(prediction))

@app.route("/predict-humans")
def predict_humans():

    diction = str(model.predict(humans))
    chunks = diction.split("'")
    prediction = chunks[1]

    return render_template("index.html", prediction_text = "The Humans has a boxoffice prediction of {}.".format(prediction))

@app.route("/predict-rocket")
def predict_rocket():

    diction = str(model.predict(rocket))
    chunks = diction.split("'")
    prediction = chunks[1]

    return render_template("index.html", prediction_text = "Red Rocket has a boxoffice prediction of {}.".format(prediction))

@app.route("/predict-song")
def predict_song():

    diction = str(model.predict(song))
    chunks = diction.split("'")
    prediction = chunks[1]

    return render_template("index.html", prediction_text = "Swan Song has a boxoffice prediction of {}.".format(prediction))

if __name__ == '__main__':
    app.jinja_env.cache = {}
    app.run(debug=True, threaded=True)