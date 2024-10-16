# Rest API Weather

Python REST API example using the weather.gov API to fetch today's forecast from specified latitude and longitude coordinates. 

## Prerequisites

To successfuly run this REST example in python, the following is required:
* Latest version of Python installed. (see [Python Downloads](https://www.python.org/downloads/ "Python Download"))
* Ensure Pip is also installed when installing Python, and relevant paths are added to your PATH so python and pip are accessible from the command line.

Next, you’ll need to install the Flask and Requests libraries from requirements.txt:
```
pip install -r requirements.txt
```

## Usage

1. Run the API using:
```
python rest-app.py
```

2. Get the Weather Forecast - You can then use a tool like curl or Postman to make a GET request to the API endpoint:
```
GET http://127.0.0.1:5000/weather?lat=39.099728&lon=-94.578568
```
NOTE:  Replace the Latitude (lat) and Longitude (lon) values with your desired coordinates.

## Response Example
The API will return a JSON response similar to:
```
{
    "short_forecast": "Sunny",
    "temperature_characterization": "moderate"
}
```