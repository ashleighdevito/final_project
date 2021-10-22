#T.Bradford
#October 2021

#Dependencies
import pandas as pd
import pickle 
import numpy as np


upcoming_movie_data = pd.read_csv('models/upcoming_movie_data.csv')

dune = upcoming_movie_data[(upcoming_movie_data['metascore'] == 75.0)].values.tolist()
ron = upcoming_movie_data[(upcoming_movie_data['metascore'] == 68.0)].values.tolist()
souvenir = upcoming_movie_data[(upcoming_movie_data['metascore'] == 98.0)].values.tolist()
spencer = upcoming_movie_data[(upcoming_movie_data['metascore'] == 85.0)].values.tolist()
mothering_sunday = upcoming_movie_data[(upcoming_movie_data['metascore'] == 69.0)].values.tolist()
humans = upcoming_movie_data[(upcoming_movie_data['imdb_rating'] == 7.3)].values.tolist()
rocket	 = upcoming_movie_data[(upcoming_movie_data['metascore'] == 78.0) & (upcoming_movie_data['imdb_rating'] == 7.0)].values.tolist()
song = upcoming_movie_data[(upcoming_movie_data['metascore'] == 66.0)].values.tolist()
