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
import xgboost
from sklearn.preprocessing import StandardScaler

model = xgboost.Booster()
model.load_model("best_xg_model.model")
# model = pickle.load(open("best_xg_model.pkl", "rb"))

movies = [dune, ron, souvenir, spencer, mothering_sunday, humans, rocket, song]
# dune = dune.reshape(-1,1)
print(model.predict(xgboost.DMatrix([dune])))



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
    
    prediction = model.predict(xgboost.DMatrix(dune))
    
    
    return render_template("index.html", prediction_text = "Dune has a boxoffice prediction of {}.".format(prediction))

@app.route("/predict-ron")
def predict_ron():
    
    prediction = model.predict(xgboost.DMatrix(ron))
    return render_template("index.html", prediction_text = "Ron's Gone Wrong has a boxoffice prediction of {}.".format(prediction))

@app.route("/predict-souvenir")
def predict_souvenir():

    prediction = model.predict(xgboost.DMatrix(souvenir))
    return render_template("index.html", prediction_text = "The Souvenir: Part II has a boxoffice prediction of {}.".format(prediction))

@app.route("/predict-spencer")
def predict_spencer():

    prediction = model.predict(xgboost.DMatrix(spencer))

    return render_template("index.html", prediction_text = "Spencer has a boxoffice prediction of {}.".format(prediction))

@app.route("/predict-mothering_sunday")
def predict_mothering():

    prediction = model.predict(xgboost.DMatrix(mothering_sunday))

    return render_template("index.html", prediction_text = "Mothering Sunday has a boxoffice prediction of {}.".format(prediction))

@app.route("/predict-humans")
def predict_humans():

    prediction = model.predict(xgboost.DMatrix(humans))

    return render_template("index.html", prediction_text = "The Humans has a boxoffice prediction of {}.".format(prediction))

@app.route("/predict-rocket")
def predict_rocket():

    prediction = model.predict(xgboost.DMatrix(rocket))

    return render_template("index.html", prediction_text = "Red Rocket has a boxoffice prediction of {}.".format(prediction))

@app.route("/predict-song")
def predict_song():

    prediction = model.predict(xgboost.DMatrix(song))

    return render_template("index.html", prediction_text = "Swan Song has a boxoffice prediction of {}.".format(prediction))

if __name__ == '__main__':
    app.jinja_env.cache = {}
    app.run(debug=True, threaded=True)