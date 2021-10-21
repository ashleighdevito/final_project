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
import boto3
import numpy as np

#Added to handle handle json not serializable error decimal return not acceptedable for jsonify
#Class creation credit to https://feryll.github.io/python/json/python-how-to-handle-json-not-serializable-error/
# class MyJSONEncoder(json.JSONEncoder):

#     def default(self, obj):
#         if isinstance(obj, decimal.Decimal):
#             # Convert decimal instances to strings.
#             return str(obj)
#         return super(MyJSONEncoder, self).default(obj)


# Create an instance of our Flask app.
app = Flask(__name__)
#app.json_encoder = MyJSONEncoder

#model = pickle.load(open("file_name", "rb"))

@app.route("/")
def home():


    # Return template and data
    return render_template("index.html")


@app.route("/index")
def index():


    # Return template and data
    return render_template("index.html")
# Set route
@app.route("/team")
def team():


    # Return template and data
    return render_template("team.html")


# Set route
@app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    return render_template("index.html", prediction_text = "boxoffice prediction {}".format(prediction))

if __name__ == '__main__':
    app.jinja_env.cache = {}
    app.run(debug=True, threaded=True)