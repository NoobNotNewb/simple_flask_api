import requests
import json

# URL of the Flask API endpoint
url = "http://127.0.0.1:5000/post_data"  # Make sure your Flask server is running on this URL

# Data to be added (you can change these values or get them from user input)
data = {
    "name": "Alice",
    "age": 25
}

# Send a POST request with the data as JSON
response = requests.post(url, json=data)

# Check the response from the server
if response.status_code == 201:
    print("Data added successfully!")
    print("Response:", response.json())
else:
    print(f"Failed to add data. Status code: {response.status_code}")
    print("Error response:", response.json())
