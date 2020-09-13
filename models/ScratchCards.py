from mongoengine import Document
from mongoengine.fields import (DateTimeField, StringField, ListField,IntField )

class ScratchCards(Document):
    meta = {'collection': 'scratch_cards'}
    date = DateTimeField()
    seri = StringField(required=True,unique=True)
    code = StringField(required=True,unique=True)

