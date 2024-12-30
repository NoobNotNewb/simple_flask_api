import requests
import json

# URL of the Flask API endpoint
url = 'http://127.0.0.1:5000/api/post_nameage'  # Change this if Flask is hosted elsewhere

# Sample data to send to the API
data = {
    "name": "Bob",
    "age": 25
}

# Send POST request to the Flask API
response = requests.post(url, json=data)

# Check if the request was successful
if response.status_code == 201:
    print("Data inserted successfully!")
else:
    print("Failed to insert data:", response.json())
