from flask import Flask, request, jsonify, render_template
from flask_pymongo import PyMongo
import json

from database_handler import DatabaseHandler
from patient import Patient
from activity import Activity

app = Flask(__name__)

with open('key.json') as f :
    config = json.load(f)
    app.config["MONGO_URI"] = config["MONGO_URI"]
mongo = PyMongo(app)
db_handler = DatabaseHandler(mongo)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/get_data', methods = ['GET'])
def get_data():
    data = list(mongo.db.newCollection.find({}, {'_id':False}))
    return jsonify(data)    

@app.route('/api/post_patient', methods=['POST'])
def post_patient():
    # Get data from the POST request
    data = request.get_json()  # Assumes the data is sent in JSON format
    new_patient = Patient.deserialize_json(data)
    #if not data or 'name' not in data or 'age' not in data:
    #   return jsonify({"error": "Invalid data"}), 400
    return db_handler.new_patient(new_patient)

# @app.route('/form')
# def form():
#     return render_template('post_data_page.html')
# @app.route('/submit', methods=['POST'])
# def submit():
#     name = request.form['name']
#     age = request.form['age']
#     return db_handler.insert_nameage(name, age)

if __name__ == '__main__':
    app.run()