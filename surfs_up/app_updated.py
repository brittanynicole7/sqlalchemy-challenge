import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt



from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the tables
measurement = Base.classes.measurement
station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return dates and precipitation values"""
    # Query all values
    one_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    data_prcp = session.query(measurement.date, measurement.prcp).filter(measurement.date >= one_year).all()

    session.close()

    # Create a dictionary from the row data and append to a list of precipitation_values
    precipitation_values = []
    for date, prcp in data_prcp:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["prcp"] = prcp
        precipitation_values.append(precipitation_dict)

    return jsonify(precipitation_values)

@app.route("/api/v1.0/stations")
def names():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all station names"""
    # Query all stations
    results = session.query(station.name).all()

    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query for the most active station
    temperatures_active = session.query(measurement.date, measurement.tobs).filter(measurement.station == 'USC00519281').all()

    session.close()

    # Create a dictionary from the row data and append to a list of temperatures_active
    active_station = []
    for date, tobs in temperatures_active:
        active_station_dict = {}
        active_station_dict["date"] = date
        active_station_dict["tobs"] = tobs
        active_station.append(active_station_dict)

    return jsonify (active_station)

@app.route("/api/v1.0/<start>")
def start(start):
     # Create our session (link) from Python to the DB
    session = Session(engine)

    # Create a start date variable with the Y,M,D format
    start_date = dt.datetime.strptime(start, "%Y-%m-%d")

    # Query for start date 
    start_query = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs))\
        .filter(measurement.date >= start_date).all()
    
    session.close()

    # Convert list of tuples into normal list
    all_temps= list(np.ravel(start_query))

    return jsonify (all_temps)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
     # Create our session (link) from Python to the DB
    session = Session(engine)

    # Create a start and end date variable with the Y,M,D format
    start_date = dt.datetime.strptime(start, "%Y-%m-%d")
    end_date = dt.datetime.strptime(end, "%Y-%m-%d")

    # Query for start and end dates
    start_query = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs))\
        .filter(measurement.date >= start_date).filter(measurement.date <= end_date).all()
    
    session.close()

    # Convert list of tuples into normal list
    all_temps= list(np.ravel(start_query))

    return jsonify (all_temps)

if __name__ == '__main__':
    app.run(debug=True)