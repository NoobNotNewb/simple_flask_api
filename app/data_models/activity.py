from mongoengine import Document, StringField, ListField, DateTimeField, FloatField, EmbeddedDocumentListField, EmbeddedDocument


class Activity(EmbeddedDocument):
    start_datetime = DateTimeField(required = False)
    duration_minutes = FloatField(required = False)
    type = StringField(required = True)
    calories = FloatField(required = False)
    image_path = StringField(required = False)
    