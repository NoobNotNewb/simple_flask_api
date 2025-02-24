from mongoengine import Document, StringField, ListField, DateTimeField, FloatField, EmbeddedDocumentListField, EmbeddedDocument


class Sleep(EmbeddedDocument):
    start_datetime = DateTimeField(required = False)
    duration_minutes = FloatField(required = True)