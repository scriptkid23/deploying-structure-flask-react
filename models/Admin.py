from mongoengine import Document
from mongoengine.fields import (DateTimeField, StringField, ListField,IntField )

class Admin(Document):
    meta = {'collection': 'admin'}
    username = StringField(required=True,unique=True)
    password = StringField(required=True,unique=True)

