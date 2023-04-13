# Tide Chart Script
This is a Python script that retrieves and displays the local tide chart for a given location using the `Tidal` API. The script takes a zip code as input and retrieves the tide data for that location. It then displays the date and time of each tide event, whether it is a high or low tide, and the height of the tide in feet.

In this example, you will need to replace `YOUR_API_KEY_HERE` with your actual API key, which you can obtain from the NOAA Tides and Currents website, `https://tidesandcurrents.noaa.gov/tide_predictions.html`. There is no way to access the NOAA's tidal data without an API key. The API key is required to authenticate your requests and ensure that you are authorized to access the data.

If you do not have an API key, you can obtain one for free from the NOAA Tides and Currents website by registering for an account. The process is straightforward and can be completed in a few minutes.

The location variable specifies the latitude and longitude of the location for which you want to retrieve the tide data. You can find the latitude and longitude of a location using tools such as `Google Maps` or `GeoPy`.

The client object is an instance of the `tidalapi.Client` class, which is used to communicate with the `NOAA Tides and Currents` API. The `get_predictions` method retrieves the tide data for the specified location and duration.

Finally, the script prints out the tide data for each day in the `tide_data` list. For each tide event, the script displays the `date` and `time`, the `type of tide` (`high` or `low`), and the `height` of the tide in feet.

## Prerequisites
To use this script, you need to have `Python 3` installed on your system, as well as the following Python libraries:

```
tidalapi
pytz
```

You also need to obtain an API key from Tidal API and set it in the script.

## Usage
To run the script, simply execute the `tide_chart.py` file after you have entered the required information into the script code.
