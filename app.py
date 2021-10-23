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
    film = "Dune"
    results = model.predict(xgboost.DMatrix([dune]))
    under = "{:.2%}".format(results[0][1])
    bin1 = "{:.2%}".format(results[0][3])
    bin2 = "{:.2%}".format(results[0][0])
    over = "{:.2%}".format(results[0][2])
    
    return render_template("results.html", film = film, under = under, bin1 = bin1, bin2 = bin2, over = over)

@app.route("/predict-ron")
def predict_ron():
    film = "Ron's Gone Wrong"
    results = model.predict(xgboost.DMatrix([ron]))
    under = "{:.2%}".format(results[0][1])
    bin1 = "{:.2%}".format(results[0][3])
    bin2 = "{:.2%}".format(results[0][0])
    over = "{:.2%}".format(results[0][2])
    return render_template("results.html", film = film, under = under, bin1 = bin1, bin2 = bin2, over = over)

@app.route("/predict-souvenir")
def predict_souvenir():
    film = "Souvenir: Part II"
    results = model.predict(xgboost.DMatrix([souvenir]))
    under = "{:.2%}".format(results[0][1])
    bin1 = "{:.2%}".format(results[0][3])
    bin2 = "{:.2%}".format(results[0][0])
    over = "{:.2%}".format(results[0][2])
    return render_template("results.html", film = film, under = under, bin1 = bin1, bin2 = bin2, over = over)

@app.route("/predict-spencer")
def predict_spencer():
    film = "Spencer"
    results = model.predict(xgboost.DMatrix([spencer]))
    under = "{:.2%}".format(results[0][1])
    bin1 = "{:.2%}".format(results[0][3])
    bin2 = "{:.2%}".format(results[0][0])
    over = "{:.2%}".format(results[0][2])
    return render_template("results.html", film = film, under = under, bin1 = bin1, bin2 = bin2, over = over)

@app.route("/predict-mothering_sunday")
def predict_mothering():
    film = "Mothering Sunday"
    results = model.predict(xgboost.DMatrix([mothering_sunday]))
    under = "{:.2%}".format(results[0][1])
    bin1 = "{:.2%}".format(results[0][3])
    bin2 = "{:.2%}".format(results[0][0])
    over = "{:.2%}".format(results[0][2])
    return render_template("results.html", film = film, under = under, bin1 = bin1, bin2 = bin2, over = over)

@app.route("/predict-humans")
def predict_humans():
    film = "The Humans"
    results = model.predict(xgboost.DMatrix([humans]))
    under = "{:.2%}".format(results[0][1])
    bin1 = "{:.2%}".format(results[0][3])
    bin2 = "{:.2%}".format(results[0][0])
    over = "{:.2%}".format(results[0][2])
    return render_template("results.html", film = film, under = under, bin1 = bin1, bin2 = bin2, over = over)

@app.route("/predict-rocket")
def predict_rocket():
    film = "Red Rocket"
    results = model.predict(xgboost.DMatrix([rocket]))
    under = "{:.2%}".format(results[0][1])
    bin1 = "{:.2%}".format(results[0][3])
    bin2 = "{:.2%}".format(results[0][0])
    over = "{:.2%}".format(results[0][2])
    return render_template("results.html", film = film, under = under, bin1 = bin1, bin2 = bin2, over = over)

@app.route("/predict-song")
def predict_song():
    film = "Swan Song"
    results = model.predict(xgboost.DMatrix([song]))
    under = "{:.2%}".format(results[0][1])
    bin1 = "{:.2%}".format(results[0][3])
    bin2 = "{:.2%}".format(results[0][0])
    over = "{:.2%}".format(results[0][2])
    return render_template("results.html", film = film, under = under, bin1 = bin1, bin2 = bin2, over = over)

if __name__ == '__main__':
    app.jinja_env.cache = {}
    app.run(debug=True, threaded=True)