import requests
import json
import datetime
from .. import constant

# URL of the Flask API endpoint
url = 'http://127.0.0.1:5000/api/post_patient'  # Change this if Flask is hosted elsewhere

# Sample data to send to the API
data = {
    "kkumail" : "doraemon",
    "first_name" : "Leon",
    "last_name" : "Kennedy",
    "phone" : "080000000",    
    # Can also use "birth_date" : 20-3-2000 (ISO 8601 format)
    "birth_date" : datetime.datetime(2000, 3, 20).strftime(constant.DATETIME_FORMAT) ,
    #"time_now" : datetime.datetime.now(),
    "height" : 160.4,
    "weight" : 60.6
}
# Send POST request to the Flask API
response = requests.post(url, json=data)

# Check if the request was successful
if response.status_code == 201:
    print("Data inserted successfully!")
else:
    print("Failed to insert data:", response.json())
