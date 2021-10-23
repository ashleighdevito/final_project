# Final Project

### Team

Thank you to Terrell Bradford, Michael Cipriani, Ashleigh DeVito, Laura Kemp, and Sam Pierce for creating this visualization.

## [Product](https://cwru-bootcamp-movie-predictor.herokuapp.com/)

This repo houses a [website](https://cwru-bootcamp-movie-predictor.herokuapp.com/) that visualizes and predicts the revenue of upcoming films based on historical movie releases from the past 15 years (2006 - Present).

### Navigation and How it Works

The top right corner of the websie includes three tabs (The Project, Our Team, and ETL Project).
The Project tab includes a detailed description of this project.
Our Team tab shows the a picture and description of each team member.
ETL Project tab is a link to our previous data bootcamp project.

The main page contains a list of upcoming moives and a "predict" button below each film. Clickling the button will generate the model and output the probability the mvoie has of grossing under $20 million, between $20 million and $100 million, between $100 million and $200 million, and above $200 million. Below is an example of the models output.

![image](static/images/example.PNG?raw=true "Dune Example")

### The Data

The team gathered data from IMDB, OMDB, Google, and The Numbers. The information obtained included movie budget data, upcoming movies, genres, buzz data, actors, etc.
The collected data was then cleaned and saved to csv files and the database was created.
AWS was used to host the database.

### The Model

The primary logic challenge of this project lied within the predictive models. The team created a Jupyter Notebook file containing the script for building the machine learning model and having it predict box office success based on the historical movie data.

The model weights are pictured here:  
![image](static/images/weights.PNG?raw=true "Weights")

### The Webpage

Heroku was used to host this application. It references this repository's root directory to build a public application.

## Process

### [Project Proposal](proposal.txt)

The goal of this project was to create a website containing a model to predict a films box office success, based on the historical movie data the team gathered.

We created sketches of what we wanted the final project to look like:

![image](static/images/napkin_drawing.jpg?raw=true "Napkin Drawing")

In the process of bulding, we diverted from these initial drawings, as we discovered limitations and decided upon other functionality. We kept the cards, but limited the results to a much smaller dataset than originally conceived, eliminating the need for pagination.

We also drafted ideas for the presentation we would be needing.

![image](static/images/presentation_sketch.jpg?raw=true "Presentation Sketch")

### Website Scraping
Example of code used to scrape from one of the data sources is shown below.
```
url = 'https://www.imdb.com/calendar/?ref_=nv_mv_cal'
response = requests.get(url)
soup = bs(response.text, 'html.parser')

lis = soup.body.find_all('li')
movies =[]
for li in lis:
                # If td element has an anchor...
    if (li.a):
                    # And the anchor has non-blank text...
        if (li.a.text):
                        # Append the td to the list
            movies.append(li)

titles =[]
for x in range(360):
    print(movies[x].text)
    titles.append(movies[x].text)
```

### Data Cleaning

Data was cleaned using jupyter notebook script.
All of the data gathered from OMDb was stored as objects, so all datatypes were converted appropriately to load into the database.
Movie titles for the upcoming released films scraped from IMDb included year of release in the string. This attribute was removed via string split.
Omitted data included: studio, language, plot, tagline, directors, writers, actors.
Release date information was converted to Month.
Features gathered from separate sources were all merged to a single dataframe on the movie title.

### Creating the Model

The creation of the model went through several interations. Our neural network model didn’t work with the pickling so we saved it as an h5 file. This proved tricky to work with and we decided to stick to using the random forest and xg boost models. Ultimately, we chose the XG boost model to use in our application.

This process included importing any models, initializing the model, fitting it to a training and testing set, performing predictions, and then measuring our model accuracy.

```
# xg boost
from xgboost import XGBClassifier

# fit model no training data
xg_model = XGBClassifier()
xg_model.fit(X_train_scaled, y_train)
```
```
# xg boost
# make predictions for test data
y_pred = xg_model.predict(X_test_scaled)
predictions = [value for value in y_pred]

from sklearn.metrics import accuracy_score
# evaluate predictions
accuracy = accuracy_score(y_test, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))
```
### Logic

The control document and the individual elements were created simultaneously by separate members of the team. They were then incorporated into one structure and deployed.  Github houses the files for any deployed webpages, Jupyter notebooks used to manipulate data, images pulled from the completed website, and other planning documentation.  Most communication was done utilizing Slack.

### Presentation

The presentation describing our project process was then created.

### Deployment

The entire repo is hosted on Heroku, and is able to be viewed publically.

## Appendix

[Heroku](https://www.heroku.com/home)
