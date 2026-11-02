CAFE & WIFI
===========

A small Flask web app for finding cafes that are good for working.
Each cafe entry records a Google Maps link, opening and closing times,
and 0-5 ratings for coffee, WiFi, and power outlets. Data is stored in
a plain CSV file, so no database is needed.


FEATURES
--------
- Landing page with a "Show Me!" button leading to the cafe list
- Add a new cafe through a validated Bootstrap-styled form
- View all cafes in a dark, striped Bootstrap table
- Map URLs are shown as clickable "Maps Link" links
- Ratings from 0 to 5 for coffee, WiFi, and power outlets


TECH STACK
----------
- Python 3
- Flask
- Bootstrap-Flask (Bootstrap5, render_form helper)
- Flask-WTF / WTForms
- Jinja2 templates


PROJECT STRUCTURE
-----------------
.
|-- main.py             Flask app, CafeForm, and routes
|-- cafe-data.csv       Cafe data, one cafe per row
|-- requirements.txt    Python dependencies
|-- templates/
|   |-- base.html       Base layout (Bootstrap loaded here)
|   |-- index.html      Landing page ("Coffee & Wifi")
|   |-- add.html        Add-cafe form (uses render_form)
|   |-- cafes.html      Table of all cafes


INSTALLATION
------------
1. Clone or download this project.

2. (Optional) Create and activate a virtual environment:

   Windows:
       python -m venv venv
       venv\Scripts\activate

   macOS / Linux:
       python3 -m venv venv
       source venv/bin/activate

3. Install the dependencies:

   Windows:
       python -m pip install -r requirements.txt

   macOS / Linux:
       pip3 install -r requirements.txt


RUNNING THE APP
---------------
    python main.py

Then open http://127.0.0.1:5000/ in your browser.


ROUTES
------
/        Landing page
/add     Form to add a cafe (GET shows the form, POST saves it)
/cafes   Table of all cafes from cafe-data.csv


CSV FORMAT
----------
Column order in cafe-data.csv:

    Cafe Name, Location URL, Open Time, Closing Time,
    Coffee Rating, WiFi Rating, Power Rating

Example row:
    Example Cafe,https://maps.app.goo.gl/example,8AM,6PM,4,3,5

The first row should be a header row with the column names.
Any value starting with "http" is displayed as a "Maps Link" link.


CONFIGURATION
-------------
The SECRET_KEY in main.py is used by Flask-WTF for CSRF protection.
Before publishing this project, move it to an environment variable:

    import os
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

Also set debug=False in app.run() for production.


FUTURE IMPROVEMENTS
-------------------
- Edit and delete cafes
- Search and sort on the cafes page
- Switch from CSV to SQLite
