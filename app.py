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
    
    results = model.predict(xgboost.DMatrix([dune]))
    under = results[0][1]
    bin1 = results[0][3]
    bin2 = results[0][0]
    over = results[0][2]
    
    return render_template("index.html", prediction_text = "The probability that Dune will have Box Office sales of \t under $20 million is: {:.2%} \n between $20 and $100 million is: {:.2%} \n between $100 million and $200 million is: {:.2%}\n above $200 million is {:.2%}.".format(under, bin1, bin2, over))

@app.route("/predict-ron")
def predict_ron():
    
    results = model.predict(xgboost.DMatrix([ron]))
    under = results[0][1]
    bin1 = results[0][3]
    bin2 = results[0][0]
    over = results[0][2]
    return render_template("index.html", prediction_text = "The probability that Ron's Gone Wrong will have Box Office sales of \t under $20 million is: {:.2%} \n between $20 and $100 million is: {:.2%} \n between $100 million and $200 million is: {:.2%}\n above $200 million is {:.2%}.".format(under, bin1, bin2, over))

@app.route("/predict-souvenir")
def predict_souvenir():

    results = model.predict(xgboost.DMatrix([souvenir]))
    under = results[0][1]
    bin1 = results[0][3]
    bin2 = results[0][0]
    over = results[0][2]
    return render_template("index.html", prediction_text = "The probability that The Souvenir: Part II will have Box Office sales of \t under $20 million is: {:.2%} \n between $20 and $100 million is: {:.2%} \n between $100 million and $200 million is: {:.2%}\n above $200 million is {:.2%}.".format(under, bin1, bin2, over))

@app.route("/predict-spencer")
def predict_spencer():

    results = model.predict(xgboost.DMatrix([spencer]))
    under = results[0][1]
    bin1 = results[0][3]
    bin2 = results[0][0]
    over = results[0][2]
    return render_template("index.html", prediction_text = "The probability that Spencer will have Box Office sales of \t under $20 million is: {:.2%} \n between $20 and $100 million is: {:.2%} \n between $100 million and $200 million is: {:.2%}\n above $200 million is {:.2%}.".format(under, bin1, bin2, over))

@app.route("/predict-mothering_sunday")
def predict_mothering():

    results = model.predict(xgboost.DMatrix([mothering_sunday]))
    under = results[0][1]
    bin1 = results[0][3]
    bin2 = results[0][0]
    over = results[0][2]
    return render_template("index.html", prediction_text = "The probability that Mothering Sunday will have Box Office sales of \t under $20 million is: {:.2%} \n between $20 and $100 million is: {:.2%} \n between $100 million and $200 million is: {:.2%}\n above $200 million is {:.2%}.".format(under, bin1, bin2, over))

@app.route("/predict-humans")
def predict_humans():

    results = model.predict(xgboost.DMatrix([humans]))
    under = results[0][1]
    bin1 = results[0][3]
    bin2 = results[0][0]
    over = results[0][2]
    return render_template("index.html", prediction_text = "The probability that The Humans will have Box Office sales of \t under $20 million is: {:.2%} \n between $20 and $100 million is: {:.2%} \n between $100 million and $200 million is: {:.2%}\n above $200 million is {:.2%}.".format(under, bin1, bin2, over))

@app.route("/predict-rocket")
def predict_rocket():

    results = model.predict(xgboost.DMatrix([rocket]))
    under = results[0][1]
    bin1 = results[0][3]
    bin2 = results[0][0]
    over = results[0][2]
    return render_template("index.html", prediction_text = "The probability that Red Rocket will have Box Office sales of \t under $20 million is: {:.2%} \n between $20 and $100 million is: {:.2%} \n between $100 million and $200 million is: {:.2%}\n above $200 million is {:.2%}.".format(under, bin1, bin2, over))

@app.route("/predict-song")
def predict_song():

    results = model.predict(xgboost.DMatrix([song]))
    under = results[0][1]
    bin1 = results[0][3]
    bin2 = results[0][0]
    over = results[0][2]
    return render_template("index.html", prediction_text = "The probability that Swan Song will have Box Office sales of \t under $20 million is: {:.2%} \n between $20 and $100 million is: {:.2%} \n between $100 million and $200 million is: {:.2%}\n above $200 million is {:.2%}.".format(under, bin1, bin2, over))

if __name__ == '__main__':
    app.jinja_env.cache = {}
    app.run(debug=True, threaded=True)