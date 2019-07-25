# Weather Checker

This Flask web app allows users to search by city or ZIP code to get current weather data and location details. Current weather data is provided 
by making calls to the Dark Sky API (https://darksky.net/dev). Location details are stored in a PostgreSQL database, which contains all ZIP codes 
in the United States that have a population of 15,000 or more. API access is provided via the `/api/<zip>` route, which returns a JSON response.

## Functionality
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

## Files
- `templates` directory: contains all the HTML templates
- `application.py`: the Flask app, which provides all the functionality listed below
- `commands.sql`: the CREATE TABLE statements used to build the PostgreSQL database used by the web site (for reference)
- `d2ujn0f3h1cj9j.sql`: a PostgreSQL dump of the database (from Adminer); data excluded
- `import.py`: used to import the locations from `zips.csv` into the PostgreSQL database
- `requirements.txt`: the necessary Python packages (Flask and SQLAlchemy, for instance) to be installed
- `zips.csv`: the 7,375 locations imported via `import.py`
- `zips_test.csv`: a smaller CSV file consisting of 4 locations used for import testing

## Origin
- Initially created as a project for CSCI S-33a Web Programming with Python and JavaScript (Harvard Summer School).
- Has since been updated and improved.