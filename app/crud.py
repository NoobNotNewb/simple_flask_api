from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import json

class CRUD :
    def __init__(self, flask_mongo):
        self.mongo = flask_mongo
    def insert_nameage(self, name, age):
        data = {
            'name' : name,
            'age' : age
        }
        result = self.mongo.db.newCollection.insert_one(data)  # Insert into 'newcollection'
        return jsonify({"message": "Data added", "id": str(result.inserted_id)}), 201