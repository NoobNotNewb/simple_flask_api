from flask import Flask, request, jsonify, render_template
import json

from database_handler import DatabaseHandler
from data_models.person import Person
from data_models.activity import Activity
from constant import MONGO_DATABASE_NAME,MONGODB_URI

app = Flask(__name__)

db_handler = DatabaseHandler()
#connect(host=MONGODB_URI)
# with open('key.json') as f :
#     config = json.load(f)
#     app.config["MONGO_URI"] = config["MONGO_URI"]
# mongo = PyMongo(app)
# db_handler = DatabaseHandler(mongo)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/get_data', methods = ['GET'])
@app.route('/get_data/<filter_field>/<value>')
def get_data(filter_field = None, value = None):
    if filter_field and value:
        person_list = db_handler.get_person({filter_field : value})
    else : 
        person_list = db_handler.get_person()
    if not person_list :
        return jsonify({})
    return jsonify(person_list)

@app.route('/api/post_person', methods=['POST'])
def post_person():
    person_data = request.get_json() 
    return db_handler.new_person(person_data)

@app.route('/api/add_activity', methods=['POST'])
def add_activity():
    data = request.get_json() 
    kkumail = data.get('kkumail', None) 
    activity_data = data.get('activity', {})
    
    if not kkumail or not activity_data :
        return jsonify({"error": "Missing required fields: kkumail or activity"}), 400
    else :
        return db_handler.add_activity(activity_data, kkumail)

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