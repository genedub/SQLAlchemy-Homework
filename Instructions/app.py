import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

import datetime as dt 

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

#reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to the tables
Measurement = Base.classes.measurement
Station = Base.classes.Station

#Create session
session = Session(engine)

app = Flask(__name__)


######################
#Flask Routes
######################

@app.route("/")
def home():
    return (
        f"All Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

@app.route('/api/v1.0/precipitation')
def home():
    return (
        year_data = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   
    data = session.query(Measurement.date, func.avg(Measurement.prcp)).\
            filter(Measurement.date.between (year_data, dt.date(2017, 8, 23))).group_by('date')
    
    prcp_data = []
    for date, prcp in data:
        prcp_dict = {}
        prcp_dict["Date"] = date
        prcp_dict["Precipitation (in)"] = round(prcp,3)
        prcp_data.append(prcp_dict)
    return jsonify(prcp_data)
    )

    @app.route("/api/v1.0/stations")
def stations():
    
    station_resultsq = session.query(Station.name).group_by(Station.station).all()
    return jsonify(s_results).all()

    session.close()

    station_list = [station[0] for station in station_resultsq]

    return jsonify(station_resultsq)


    @app.route("/api/v1.0/tobs")
def tobs ():
    
    recent_date_dt = dt.datetime.strptime(recent_date, "%Y-%m-%d")
    one_yr = recent_date_dt - dt.timedelta(days=365)
    one_yr_dt = dt.datetime.strftime(one_yr,"%Y-%m-%d")

    months_data = session.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.station =='USC00519281').\
    filter(Measurement.date > one_yr_dt).all()

     temp_list = [temp[1] for temp in months_data]

    return jsonify(temp_list)

    
    # Create list of temperature
    temp_list = [temp[1] for temp in months_data]

    return jsonify(temp_list)

    if __name__ == '__main__':
    app.run(debug=True)


