from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import json
from datetime import datetime
from typing import Optional

from patient import Patient
from activity import Activity

class DatabaseHandler :
    def __init__(self, flask_mongo):
        self.mongo = flask_mongo
        
    def new_patient(self, patient):
        patient_data = patient.serialize_json()
        result = self.mongo.db.newCollection.insert_one(patient_data)  # Insert into 'newcollection'
        return jsonify({"message": "Data added", "id": str(result.inserted_id)}), 201
    
    # Can add filter later?
    def get_patient(self, filter :Optional[dict] = None):
        if filter :
            patient_data_list = list(self.mongo.db.newCollection.find(filter,{'_id' : False}))
        else :
            patient_data_list = list(self.mongo.db.newCollection.find({},{'_id' : False}))
        patient_list = []
        if not patient_data_list:
            return None    
        for patient_data in patient_data_list :
            # Deserialize the patient data
            patient = Patient.deserialize_json(patient_data)
            # Add activities if any
            for activity_data in patient_data.get("activities", []):
                activity = Activity.deserialize_activity(activity_data)
                patient.add_activity(activity)
            patient_list.append(patient)
        return patient_list

    def add_activity(self, activity : Activity, kkumail : str):
        print("add Activity")