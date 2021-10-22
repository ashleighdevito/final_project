#T.Bradford
#October 2021

#Dependencies
import pandas as pd
import pickle 
import numpy as np


upcoming_movie_data = pd.read_csv('scaled_upcoming_data.csv')
    
dune = upcoming_movie_data.iloc[0]
ron = upcoming_movie_data.iloc[1]
souvenir = upcoming_movie_data.iloc[2]
spencer = upcoming_movie_data.iloc[3]
mothering_sunday = upcoming_movie_data.iloc[4]
humans = upcoming_movie_data.iloc[5]
rocket	 = upcoming_movie_data.iloc[6]
song = upcoming_movie_data.iloc[7]
