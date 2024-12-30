from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/newdatabase"
mongo = PyMongo(app)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/get_data', methods = ['GET'])
def get_data():
    data = list(mongo.db.newCollection.find({}, {'_id':False}))
    return jsonify(data)

@app.route('/post_data', methods=['POST'])
def post_data():
    data = request.json  # Get data from POST request
    result = mongo.db.newCollection.insert_one(data)  # Insert into 'newcollection'
    return jsonify({"message": "Data added", "id": str(result.inserted_id)}), 201

if __name__ == '__main__':
    app.run()