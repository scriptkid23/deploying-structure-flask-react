from mongoengine import Document
from mongoengine.fields import (DateTimeField, StringField, ListField,IntField )

class Challenges(Document):
    meta = {'collection': 'challenges'}
    date = DateTimeField()
    challenge = ListField(ListField(IntField()))

