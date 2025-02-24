#datetime format as string in ISO 8601 but manually create so can be changed later
# 20-3-2020T06:16:42+12:00 (%Date-%Month-%YearT%Hour%Minute%Second%UTC-offset)
DATETIME_FORMAT = "%d-%m-%YT%H:%M:%S%z"
MONGO_DATABASE_NAME = "healthy_kku"
MONGODB_URI = "mongodb://localhost:27017/" + MONGO_DATABASE_NAME 
