from flask import Flask, request, jsonify, url_for, render_template
from flask_pymongo import PyMongo
import json

from crud import CRUD

app = Flask(__name__)

with open('key.json') as f :
    config = json.load(f)
    app.config["MONGO_URI"] = config["MONGO_URI"]
mongo = PyMongo(app)
crud_instance = CRUD(mongo)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/get_data', methods = ['GET'])
def get_data():
    data = list(mongo.db.newCollection.find({}, {'_id':False}))
    return jsonify(data)    

@app.route('/form')
def form():
    return render_template('post_data_page.html')
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']
    return crud_instance.insert_nameage(name, age)

@app.route('/api/post_nameage', methods=['POST'])
def post_nameage():
    # Get data from the POST request
    data = request.get_json()  # Assumes the data is sent in JSON format

    if not data or 'name' not in data or 'age' not in data:
        return jsonify({"error": "Invalid data"}), 400

    return crud_instance.insert_nameage(data['name'], data['age'])


if __name__ == '__main__':
    app.run()