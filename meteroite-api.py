from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from configparser import ConfigParser
from sqlalchemy import create_engine, text
import pandas as pd

app = Flask(__name__)

# Read database configuration from config.ini
config = ConfigParser()
config.read('config.ini')

# Configure Flask app
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(username)s:%(password)s@%(host)s:%(port)s/%(database)s' % {
    'username': config['database']['username'],
    'password': config['database']['password'],
    'host': config['database']['host'],
    'port': config['database']['port'],
    'database': config['database']['database']
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define SQLAlchemy engine
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

# API to retrieve a full list of company info from the companies table
@app.route("/meteorite/location-mass")
def get_mass():
    # Use a with statement to ensure the connection is closed after the query
    with engine.connect() as conn:
        query = text("SELECT name, mass, latitude, longitude FROM meteorite;")
        df_mass_name = pd.read_sql(query, conn)

   # Convert the DataFrame to JSON and return
    return df_mass_name.to_json(orient="records")

@app.route("/meteorite/name-comp")
def get_comp():
    # Use a with statement to ensure the connection is closed after the query
    with engine.connect() as conn:
        query = text("SELECT name, classification FROM meteorite;")
        df_name_comp = pd.read_sql(query, conn)

   # Convert the DataFrame to JSON and return
    return df_name_comp.to_json(orient="records")

# @app.route("/meteorite/name-comp")
# def get_comp():
#     # Use a with statement to ensure the connection is closed after the query
#     with engine.connect() as conn:
#         query = text("SELECT name, classification FROM meteorite;")
#         df_name_comp = pd.read_sql(query, conn)

#    # Convert the DataFrame to JSON and return
#     return df_name_comp.to_json(orient="records")

if __name__ == '__main__':
    app.run(debug=True)