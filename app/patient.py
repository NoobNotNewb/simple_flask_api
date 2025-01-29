from datetime import datetime
from typing import Optional, List
import json

from activity import Activity
from constant import DATETIME_FORMAT


class Patient:
    def __init__(self, 
                 kkumail : str,
                 first_name : str, 
                 last_name:str,
                 phone : str,
                 birth_date : datetime,
                 height : float,
                 weight : float,
                 activities: Optional[List['Activity']] = None
                 ):
        self.kkumail = kkumail
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.birth_date = birth_date
        self.height = height
        self.weight = weight
        # Use an empty list if no activities are provided (i.e., activities is None)
        self.activities = activities if activities is not None else []
    
    def add_activity(self, activity : 'Activity'):
        self.activities.append(activity)
    
    def serialize_json(self) :
        patient_data = {
            "kkumail" : self.kkumail,
            "first_name" : self.first_name,
            "last_name" : self.last_name,
            "phone" : self.phone,
            "birth_date" : self.birth_date.strftime(DATETIME_FORMAT),
            "height" : self.height,
            "weight" : self.weight,
            "activities" : [activity.serialize_json for activity in self.activities]
        }
        return patient_data
    
    @classmethod
    def deserialize_json(cls, patient_data : 'json') :
        activities = [Activity.deserialize_json(activity) for activity in patient_data.get("activities",[])]
        patient = cls(            
            kkumail = patient_data["kkumail"],
            first_name = patient_data["first_name"],
            last_name = patient_data["last_name"],
            phone = patient_data["phone"],
            birth_date = datetime.strptime(patient_data["birth_date"], DATETIME_FORMAT),
            height = patient_data["height"],
            weight = patient_data["weight"],
            activities = activities
            )
        return patient
    