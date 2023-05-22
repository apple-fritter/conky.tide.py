# tide.py
This is a Python script that retrieves and displays the local tide chart for a given location using the `Tidal` API. The script takes a zip code as input and retrieves the tide data for that location. It then displays the date and time of each tide event, whether it is a high or low tide, and the height of the tide in feet.

In this example, you will need to replace `YOUR_API_KEY_HERE` with your actual API key, which you can obtain from the NOAA Tides and Currents website, `https://tidesandcurrents.noaa.gov/tide_predictions.html`. There is no way to access the NOAA's tidal data without an API key. The API key is required to authenticate your requests and ensure that you are authorized to access the data.

If you do not have an API key, you can obtain one for free from the NOAA Tides and Currents website by registering for an account. The process is straightforward and can be completed in a few minutes.

The location variable specifies the latitude and longitude of the location for which you want to retrieve the tide data. You can find the latitude and longitude of a location using tools such as `Google Maps` or `GeoPy`.

The client object is an instance of the `tidalapi.Client` class, which is used to communicate with the `NOAA Tides and Currents` API. The `get_predictions` method retrieves the tide data for the specified location and duration.

Finally, the script prints out the tide data for each day in the `tide_data` list. For each tide event, the script displays the `date` and `time`, the `type of tide` (`high` or `low`), and the `height` of the tide in feet.

---

## Prerequisites
To use this script, you need to have `Python 3` installed on your system, as well as the following Python libraries:

```
tidalapi
pytz
```

You also need to obtain an API key from Tidal API and set it in the script.

---

## Usage
To run the script, simply execute the `tide_chart.py` file after you have entered the required information into the script code. Saving your .conkyrc while an instance of Conky is running will cause it to restart and execute any properly referenced scripts.

---

## 🤪 Conky Meta

- [888v](https://github.com/apple-fritter/888v): Virtual webcam clone with Conky overlay; Bash.
- [.conkyrc](https://github.com/apple-fritter/.conkyrc): conky configuration file.
- [moonphase.py](https://github.com/apple-fritter/conky.moonphase.py): RSS reader for Conky that reads in a TSV based list of feeds. Python.
- [RTSP-view.py](https://github.com/apple-fritter/conky.RTSP-view.py): Script that displays an RTSP stream. Python.
- [tide.py](https://github.com/apple-fritter/conky.tide.py): Script that displays the local tide using the Tidal API. Python.
- [twitter.py](https://github.com/apple-fritter/conky.twitter.py): Script that displays a user's Twitter notifications. Python.

---

## [Disclaimer](DISCLAIMER)
**This software is provided "as is" and without warranty of any kind**, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

**The authors do not endorse or support any harmful or malicious activities** that may be carried out with the software. It is the user's responsibility to ensure that their use of the software complies with all applicable laws and regulations.

---

## License

These files released under the [MIT License](LICENSE).
