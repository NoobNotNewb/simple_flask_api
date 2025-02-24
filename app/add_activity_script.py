import requests
import json
import datetime
import constant

# URL of the Flask API endpoint
url = 'http://127.0.0.1:5000/api/add_activity'  # Change this if Flask is hosted elsewhere

# Sample data to send to the API
data = {
    "kkumail" : "doraemon",
    "activity" : {
        "start_datetime" : "23-2-2025T00:00:00",
        "duration_minutes" : "30",
        "type" : "ref_to_activity_type?",
        "calories" : "50",
        "image_path" : "asdfjka"
    }
}
# Send POST request to the Flask API
response = requests.post(url, json=data)

# Check if the request was successful
if response.status_code == 200:
    print("Data update successfully!")
else:
    print("Failed to update data:", response.json())
