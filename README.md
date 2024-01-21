# Meteorite Landings Data Analysis and Visualization Project

## Project Overview

This project involves analyzing and visualizing meteorite landing data. The workflow includes cleaning and processing data in a Jupyter Notebook, developing a Flask API in Visual Studio Code, and creating an interactive dashboard using JavaScript and CSS.

### Data Cleaning and Processing (Jupyter Notebook)

- **Dependencies**: `Pandas` for data manipulation.
- **Data Source**: CSV file with meteorite landing data.
- **Cleaning Steps**:
  - Drop rows with missing data.
  - Convert 'year' column to integer.
  - Remove invalid coordinates (e.g., 0,0).
  - Rename columns for clarity.
  - Reset index after cleaning.

### Flask API Development (Visual Studio Code)

- **Dependencies**: `Flask`, `Flask_SQLAlchemy`, `ConfigParser`, `SQLAlchemy`.
- **Configuration**: Database credentials are stored in `config.ini`.
- **API Endpoints**:
  - `/meteorite/location-mass`: Returns meteorite name, mass, latitude, and longitude.
  - `/meteorite/name-parent_class`: Returns meteorite name and parent classification.

### Dashboard Development (JavaScript and CSS)

- **Technologies**: HTML, Leaflet.js (for mapping), D3.js (for charting).
- **Features**:
  - Interactive map showing meteorite landings.
  - Bar chart displaying top meteorite classifications.
- **Styling**: CSS for the layout and design of the dashboard components.

### File Structure

- `cleaned_meteorite_landing.csv`: Cleaned and processed meteorite data.
- `app.py`: Flask API script.
- `config.ini`: Database configuration file.
- `index.html`: Main dashboard HTML file.
- `styles.css`: Stylesheet for the dashboard.
- `script.js`: JavaScript for interactive elements.

### Instructions for Running the Project

1. **Data Cleaning**:
   - Open the Jupyter Notebook.
   - Run all cells to clean and process the data.
   - The cleaned data is saved as `cleaned_meteorite_landing.csv`.
2. **Flask API**:
   - Open `app.py` in Visual Studio Code.
   - Update `config.ini` with your database credentials.
   - Run `app.py` to start the Flask server.
3. **Dashboard**:
   - Open `index.html` in a browser to view the dashboard.
   - Use the interactive map and bar chart to explore meteorite data.

### Additional Notes

- Ensure all dependencies are installed for the Jupyter Notebook and Flask API.
- The Flask API must be running to fetch data for the dashboard.
- Update the dashboard's fetch URLs to point to your Flask API endpoints.
