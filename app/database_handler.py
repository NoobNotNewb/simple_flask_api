from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import json
from datetime import datetime
from patient import Patient

class DatabaseHandler :
    def __init__(self, flask_mongo):
        self.mongo = flask_mongo
        
    def new_patient(self, patient):
        patient_data = patient.serialize_json()
        result = self.mongo.db.newCollection.insert_one(patient_data)  # Insert into 'newcollection'
        return jsonify({"message": "Data added", "id": str(result.inserted_id)}), 201
    
    def get_patient(self, kkumail : str):
        patient_data = self.collection.find_one({"kkumail": kkumail})
        if patient_data:
            # Deserialize the patient data
            patient = Patient.deserialize_json(patient_data)
            # Add activities if any
            for activity_data in patient_data.get("activities", []):
                activity = self.deserialize_activity(activity_data)
                patient.add_activity(activity)
            return patient
        return None
