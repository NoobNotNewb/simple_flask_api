from datetime import datetime
from typing import Optional

from constant import DATETIME_FORMAT

class Activity():
    def __init__(self, 
                activity_datetime : datetime, 
                activity_name : str,
                calories : Optional[float] = None):
        self.activity_datetime = activity_datetime
        self.activity_name = activity_name
        self.calories = calories
        
    def serialze_json(self):
        activity_data = {
            "activity_datetime" : self.activity_datetime.strftime(DATETIME_FORMAT),
            "activity_name" : self.activity_name,
            "calories" : self.calories
        }
        return activity_data
    
    @classmethod
    def deserialize_json(cls, activity_data):
        activity = cls(
            activity_datetime = datetime.strptime(activity_data["activity_datetime"], DATETIME_FORMAT),
            activity_name = activity_data["activity_name"],
            calories = activity_data["calories"]
        )
        return activity
    
    