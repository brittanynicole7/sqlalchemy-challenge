# SQL Alchemy Challenge

# Project Description 

## Part 1: Analyze and Explore Climate Data

### Connect Jupyter Notebook to Database
- Connect to a SQLite database using SQLAlchemy
- Reflect tables into classes using SQLAlchemy
- Save classes as station and measurement
- Link Python to the database by creating a SQLAlchemy session
- Close the session

### Precipitation Analysis
- Query for the most recent date in the dataset
- Query for date and precipitation values over the last year and save them to a DataFrame
- Sort the DataFrame by date
- Plot the results 
- Print the summary statistics for the precipitation data

### Station Analysis
- Query for the number of stations in the dataset
- Query for the stations and observations counts in descending order and find the most active station
- Query for the min, max, and average temperatures for the most acitve station
- Query for the previous 12 months of temperature data for the most active station
- Plot these values in a histogram

## Part 2: Design a Climate App
- Design a climate app using Flask that lists the following routes
        - /api/v1.0/precipitation
        - /api/v1.0/stations
        - /api/v1.0/tobs
        - /api/v1.0/start
        - /api/v1.0/start/end
- For the precipitation route, convert the query results from the precipitation analysis (retrieving the last 12 months of data) to a dictionary and jsonify the dictionary values.
- For the stations route, return a JSON list of the stations.
- For the tobs route, query the dates and temperatures for the most active station and return a JSON list of the temperature observations.
- For the start route, return the minimum, average, and maximum temperature observations of all dates greater than or equal to a start date and return a jsonified list. 
- For the start/end route, return the minimum, average, and maximum temperature observations of all dates between a specified start and end date and return a jsonified list. 

# Software and Files
## For the Precipitation and Station Analysis/SQLAlchemy and ORM
- %matplotlib inline
- from matplotlib import style
- style.use('fivethirtyeight')
- import matplotlib.pyplot as plt
- import numpy as np
- import pandas as pd
- import datetime as dt
- import sqlalchemy
- from sqlalchemy.ext.automap import automap_base
- from sqlalchemy.orm import Session
- from sqlalchemy import create_engine, func

## For the Climate App 
- import numpy as np
- import sqlalchemy
- from sqlalchemy.ext.automap import automap_base
- from sqlalchemy.orm import Session
- from sqlalchemy import create_engine, func
- import datetime as dt
- from flask import Flask, jsonify

# Output/Analyses



# Author 
-Brittany Wright github:brittanynicole7
