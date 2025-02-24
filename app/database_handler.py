from flask import jsonify
from mongoengine import connect, NotUniqueError
from typing import Optional
from datetime import datetime

from data_models.person import Person
from data_models.activity import Activity
from data_models.sleep import Sleep
from constant import MONGODB_URI, DATETIME_FORMAT
from datetime_parser import DateTimeParser

connect(host=MONGODB_URI)

class DatabaseHandler :
    def __init__(self):
        connect(host = MONGODB_URI)
        self.dt_parser = DateTimeParser()
        print("Connected to database")
        
    def new_person(self, person_data):
        person = Person(
            kkumail = person_data.get('kkumail'),
            first_name = person_data.get('first_name'),
            last_name = person_data.get('last_name'),
            nickname = person_data.get('nickname'),
            phone = person_data.get('phone'),
            sex = person_data.get('sex'),
            birth_date = self.dt_parser.parse(person_data.get('birth_date')),
            height  = person_data.get('height'),
            weight = person_data.get('weight'),
            institution = person_data.get('institution'),
            image_path = person_data.get('image_path'),
            activities = person_data.get('activities',[])
        )
        try :
            saved_person = person.save()
            return jsonify({"message": "Data added", "id": str(saved_person.id)}), 201
        except NotUniqueError:
            return jsonify({"error": "Email is already taken. Please use a different email."}), 409       

    def get_person(self, filter_field = "kkumail", value = None):
        person_query = None
        if filter_field and value:
            pass # Will probably need to use direct mongo query in mongoengine in this case
        elif value and filter_field == "kkumail" :
            person_query = Person.objects(kkumail = value)
        else :
            person_query = Person.objects()

        person_list = []
        for person in person_query:
            person_dict = person.to_mongo()  # Convert document to dictionary
            person_dict['_id'] = str(person_dict['_id'])  # Convert ObjectId to string
            person_list.append(person_dict)
        return person_list
    
    def add_activity(self, activity_data , kkumail : str):
        activity = Activity(
            start_datetime = activity_data.get('start_datetime'),
            duration_minutes = activity_data.get('duration_minutes'),
            type = activity_data.get('type'),
            calories = activity_data.get('calories'),
            image_path = activity_data.get('image_path')
        )
        result = Person.objects(kkumail = kkumail).update(add_to_set__activities = activity)
        if result > 0:  # If at least one document was updated
            return jsonify({"message": "Activity added successfully!"}), 200
        else:
            return jsonify({"message": "Activity was already added(duplicated \'_id\') or no matching person found."}), 409
        
    def add_sleep(self, sleep_data , kkumail : str):
        sleep = Sleep(
            start_datetime = sleep_data.get('start_datetime'),
            duration_minutes = sleep_data.get('duration_minutes')
        )
        result = Person.objects(kkumail = kkumail).update(add_to_set__sleeps = sleep)
        
        if result > 0:  # If at least one document was updated
            return jsonify({"message": "Activity added successfully!"}), 200
        else:
            return jsonify({"message": "Activity was already added(duplicated) or no matching person found."}), 409
    

