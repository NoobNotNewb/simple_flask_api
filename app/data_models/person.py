from mongoengine import Document, StringField, ListField, DateTimeField, FloatField, EmbeddedDocumentListField

from data_models.activity import Activity
from data_models.sleep import Sleep


class Person(Document):
    kkumail = StringField(unique = True)
    first_name = StringField(required = True)
    last_name = StringField(required = True)
    nickname = StringField(required = False)
    phone = StringField(required = True)
    sex = StringField(required = True)
    birth_date = DateTimeField(required = True)
    height = FloatField(required = True)
    weight = FloatField(required = True)
    institution = StringField(required = False)
    image_path = StringField(required = False)
    activities = EmbeddedDocumentListField(Activity,required = False)
    sleeps = EmbeddedDocumentListField(Sleep, required = False)