import tidalapi
from datetime import datetime, timedelta

# Set your API key
api_key = 'YOUR_API_KEY_HERE'

# Set the location for which you want to retrieve the tide data
location = tidalapi.Location(47.608013, -122.335167)  # Seattle, WA

# Initialize the Tidal API client
client = tidalapi.Client(api_key)

# Get today's date and time
today = datetime.now()

# Set the start and end times for the tide data query
start_time = today.replace(hour=0, minute=0, second=0, microsecond=0)
end_time = today.replace(hour=23, minute=59, second=59, microsecond=0)

# Retrieve the tide data for today
tide_data = client.get_predictions(location, 1, start_time, end_time)

# Print the tide data
for tide in tide_data:
    print(tide.dt_str, tide.type.name, tide.height_ft)
