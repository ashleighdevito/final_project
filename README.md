# Final Project

### Team

Thank you to Terrell Bradford, Michael Cipriani, Ashleigh DeVito, Laura Kemp, and Sam Pierce for creating this visualization.

## [Product](insert website here)

This repo houses a [website](insert website here) that visualizes and predicts the revenue of upcoming films based on historical movie releases from the past 15 years (2006 - Present).

### Navigation
 
  Top Navigation..
  Side Bar..
  Upcoming Movies..
  Analysis..
  Team Page..

## How It Works

### The Data

The team gathered data from IMDB, OMDB, Google, and The Numbers. The information obtained included movie budget data, upcoming movies, genres, buzz data, actors, etc.
The collected data was then cleaned and saved to csv files and the database was created.
AWS was used to host the database

### The Model

The primary logic challenge of this project lied within the predictive models. The team created a Jupyter Notebook file containing the script for building the machine learning model and having it predict box office success based on the historical movie data.

The model weights are pictured here:![image](static/images/weights.PNG?raw=true "Weights")

### The Webpage

Heroku was used to host this application. It references this repository's root directory to build a public application.

## Process

### [Project Proposal](proposal.txt)

The goal of this project was to create a website that contained a model that could predict a films box office success based on the historical movie data the team gathered.

We created sketches of what we wanted the final project to look like:

![image](static/images/napkin_drawing.jpg?raw=true "Napkin Drawing")

In the process of bulding, we diverted from these initial drawings, as we discovered limitations and decided upon other functionality.

We also drafted ideas for the presentation we would be needing.

![image](static/images/presentation_sketch.jpg?raw=true "Presentation Sketch")

### Data Cleaning


### Creating the Model

Using a Jupiter notebook, queries were run to create a materialized view within our database.

```

```

Next Flask was used to create routes to this view, hosted on Heroku. Below is one of three routes we created.

```

    
```
### Logic

The control document and the individual elements were created simultaneously by separate members of the team.  They were then incorporated into one structure and deployed.

### Testing

We then examined the data and debugged any issues.  Several that we ran into:

1. 
2. 
3. 
4. 
5. 
6. 

### Presentation

The presentation was then created and repo organized.

### Deployment

The entire repo is hosted on Heroku, and is able to be viewed publically.

## Appendix

[Awesome Markers leaflet library](https://github.com/lennardv2/Leaflet.awesome-markers)  
[Heroku](https://www.heroku.com/home)
