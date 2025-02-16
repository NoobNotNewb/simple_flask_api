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
@app.route('/get_data/<filter_field>/<value>')
def get_data(filter_field = None, value = None):
    if filter_field and value:
        patient_list = db_handler.get_patient({filter_field : value})
    else : 
        patient_list = db_handler.get_patient()
    data = []
    if not patient_list :
        return jsonify({})
    for patient in patient_list :
        data.append(patient.serialize_json())
    return jsonify(data)    

@app.route('/api/post_patient', methods=['POST'])
def post_patient():
    # Get data from the POST request
    data = request.get_json() 
    new_patient = Patient.deserialize_json(data)
    return db_handler.new_patient(new_patient)

@app.route('/api/add_activity', methods=['POST'])
def add_activity():
    # Get data from the POST request
    data = request.get_json() 
    kkumail = data.get('kkumail', None) 
    activity_data = data.get('activity', {})
    if not kkumail or not activity_data :
        return 
    new_activity = Activity.deserialize_json(activity_data)
    return db_handler.add_activity(new_activity, kkumail)

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