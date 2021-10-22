# Final Project

### Team

Thank you to Terrell Bradford, Michael Cipriani, Ashleigh DeVito, Laura Kemp, and Sam Pierce for creating this visualization.

## [Product](insert website here)

This repo houses a [website](insert website here) that visualizes and predicts the revenue of upcoming films based on historical movie releases from the past 15 years (2006 - Present).

### Navigation
 
  Top Navigation
  Side Bar
  Upcoming Movies
  Analysis
  Team Page

## How It Works

### The Model(s)

The primary logic challenge of this project lied within the predictive model.  We have a Jupyter Notebook file containing the script for building the machine learning model and having it predict box office success based on the historical movie data. The data works as follows:

1....
2....
3....

### The Webpage

Heroku was used to host this application. It references this repository's root directory to build a public application.

## Process

### [Project Proposal](proposal.txt)

The goal of this project was to create a website that contained a model that could predict a films box office success based on the historical movie data the team gathered.

We created sketches of what we wanted the final project to look like:

![image](static/images/napkin_drawing.jpg?raw=true "Napkin Drawing")

In the process of bulding, we diverted from these initial drawings, as we discovered limitations and decided upon other functionality.

We also drafted ideas for the presentation we would be needing.

![image](insert presentation image here)

### Data Cleaning


### Creating the API

Using a Jupiter notebook, queries were run to create a materialized view within our database.

```
engine = create_engine(f'postgresql://{Username}:{Password}@{Host}:5432/{DB}', echo=False)
connection = engine.connect()

cursor = engine.execute('CREATE MATERIALIZED VIEW accidentcounty AS 
SELECT public."Lat_Lng"."Accident_ID",   public."Lat_Lng"."Start_Lat",public."Lat_Lng"."Start_Lng",public."NY_Accidents"."Severity",public."Time"."Start_Time",public."Time"."End_Time",public."Time"."Sunrise_Sunset", public."Infrastructure"."Bump", public."Infrastructure"."Crossing", public."Infrastructure"."Give_Way", public."Infrastructure"."Junction", public."Infrastructure"."Railway", public."Infrastructure"."Roundabout", public."Infrastructure"."Station", public."Infrastructure"."Stop", public."Infrastructure"."Traffic_Calming", public."Infrastructure"."Traffic_Signal", public."Infrastructure"."Turning_Loop", public."Weather"."Weather_Timestamp", public."Weather"."Temperature", public."Weather"."Wind_Chill", public."Weather"."Humidity", public."Weather"."Pressure", public."Weather"."Visibility", public."Weather"."Wind_Direction", public."Weather"."Wind_Speed", public."Weather"."Precipitation", public."Weather"."Weather_Condition", public."Address"."City", public."Address"."Zipcode", public."Address"."County_ID", public."County"."County_Name" 
FROM public."Lat_Lng" 
LEFT JOIN public."NY_Accidents" ON public."Lat_Lng"."Accident_ID" = "NY_Accidents"."Accident_ID" 
LEFT JOIN public."Time" ON public."Lat_Lng"."Accident_ID" = "Time"."Accident_ID" 
LEFT JOIN public."Infrastructure" ON public."Lat_Lng"."Accident_ID" = "Infrastructure"."Accident_ID" 
LEFT JOIN public."Weather" ON public."Lat_Lng"."Accident_ID" = "Weather"."Accident_ID" 
LEFT JOIN public."Address" ON public."Lat_Lng"."Accident_ID" = "Address"."Accident_ID" 
LEFT JOIN public."County" ON public."Address"."County_ID" = "County"."County_ID"   
WHERE public."Address"."County_ID" = 85 
OR public."Address"."County_ID" =47 
OR public."Address"."County_ID" = 61 
OR public."Address"."County_ID" =5 
OR public."Address"."County_ID" =81').fetchall()

```

Next Flask was used to create routes to this view, hosted on Heroku. Below is one of three routes we created.

```

@app.route('/api/geojson')
def geojson():  
    #cursor = engine.execute('SELECT public."Lat_Lng"."Accident_ID", public."Lat_Lng"."Start_Lat",public."Lat_Lng"."Start_Lng",public."NY_Accidents"."Severity",public."Time"."Start_Time",public."Time"."End_Time",public."Time"."Sunrise_Sunset", public."Infrastructure"."Bump", public."Infrastructure"."Crossing", public."Infrastructure"."Give_Way", public."Infrastructure"."Junction", public."Infrastructure"."Railway", public."Infrastructure"."Roundabout", public."Infrastructure"."Station", public."Infrastructure"."Stop", public."Infrastructure"."Traffic_Calming", public."Infrastructure"."Traffic_Signal", public."Infrastructure"."Turning_Loop", public."Weather"."Weather_Timestamp", public."Weather"."Temperature", public."Weather"."Wind_Chill", public."Weather"."Humidity", public."Weather"."Pressure", public."Weather"."Visibility", public."Weather"."Wind_Direction", public."Weather"."Wind_Speed", public."Weather"."Precipitation", public."Weather"."Weather_Condition", public."Address"."City", public."Address"."Zipcode", public."Address"."County_ID", public."County"."County_Name" FROM public."Lat_Lng" LEFT JOIN public."NY_Accidents" ON public."Lat_Lng"."Accident_ID" = "NY_Accidents"."Accident_ID" LEFT JOIN public."Time" ON public."Lat_Lng"."Accident_ID" = "Time"."Accident_ID" LEFT JOIN public."Infrastructure" ON public."Lat_Lng"."Accident_ID" = "Infrastructure"."Accident_ID" LEFT JOIN public."Weather" ON public."Lat_Lng"."Accident_ID" = "Weather"."Accident_ID" LEFT JOIN public."Address" ON public."Lat_Lng"."Accident_ID" = "Address"."Accident_ID" LEFT JOIN public."County" ON public."Address"."County_ID" = "County"."County_ID"').fetchall()
    #cursor = engine.execute('SELECT * FROM public.mymatview').fetchall()

    #query database
    cursor = engine.execute('SELECT "Start_Lat","Start_Lng","Start_Time","Severity","County_Name" FROM public.accidentcounty LIMIT 5000').fetchall()

    #format geojson loop through database query and append data
    geo_json = []
    content = {}
    for result in cursor:
        content = {'Type':'Feature',
                    'Geometry':{'Type':'Point',
                    'Coordinates': [result['Start_Lat'],result['Start_Lng']]
                    },
                    'Properties':{
                        'Severity': result['Severity'],
                        'County': result['County_Name'],
                        'Time': result['Start_Time']

                    }

        }
         #append data         
        geo_json.append(content)
        content = {}
    #return Data
    return jsonify(geo_json) 
```
### Logic

The control document and the individual elements were created simultaneously by separate members of the team.  They were then incorporated into one structure and deployed.

### Testing

We then examined the data and debugged any issues.  Several that we ran into:

1. Determining how to deploy the repo, as Heroku needed config files to operate.
2. Having to reexamine the ETL process due to a bug in the previous project.
3. Clearing the map layers between selections on the sidebar.
4. Correcting data types among feature properties.
5. Optimizing performance through the size of the API call.
6. Working between the utilized libraries and Heroku to ensure proper deployment.

### Presentation

The presentation was then created and repo organized.

### Deployment

The entire repo is hosted on Heroku, and is able to be viewed publically.

## Appendix

[Awesome Markers leaflet library](https://github.com/lennardv2/Leaflet.awesome-markers)  
[Heroku](https://www.heroku.com/home)
