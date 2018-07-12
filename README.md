# Project 1

Web Programming with Python and JavaScript

This web site allows users to query weather information via the Dark Sky API (https://darksky.net/dev). You can search for a
location by its ZIP code or city/town name. All ZIP codes in the United States that have a population of 15,000 or more are included
here.

Files:
- `templates` directory: contains all the HTML templates
- `application.py`: the Flask app, which provides all the functionality listed below
- `commands.sql`: the CREATE TABLE statements used to build the PostgreSQL database used by the web site (for reference)
- `import.py`: used to import the locations from `zips.csv` into the PostgreSQL database
- `requirements.txt`: the necessary Python packages (Flask and SQLAlchemy, for instance) to be installed
- `zips.csv`: the 7,375 locations imported via `import.py`
- `zips_test.csv`: a smaller CSV file consisting of 4 locations used for import testing

Functionality:
- Register for an account
- Login/logout
- Search: Search for a location by ZIP code or city/town name (partial matching supported, e.g. "2138" will find "02138")
- Check-In Submission: When viewing a specific location, users who are logged in can submit a “check-in” to log a visit (one
check-in per user for a given location) along with a free-text comment about the location
- Location Data: The location page displays location details (location name, ZIP code, latitude, longitude, population, and the number of
check-ins), current weather data (time of weather report, textual weather summary e.g. “Clear”, temperature, dew point, and
humidity), and comments that users have left for that location
- API Access: Users can make a GET request via the `/api/<zip>` route, where `<zip>` is a ZIP code. If the requested ZIP code isn’t
in the database, a 404 error is returned. Example of a JSON response:
```json
{
    "place_name": "Cambridge",
    "state": "MA",
    "latitude": 42.37,
    "longitude": -71.11,
    "zip": "02138",
    "population": 36314,
    "check_ins": 1
}
```
