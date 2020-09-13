from mongoengine import Document
from mongoengine.fields import (DateTimeField, ReferenceField )
from models.Challenges import Challenges
from models.ScratchCards import ScratchCards
class Store(Document):
    meta = {'collection': 'store'}
    date = DateTimeField()
    challenge = ReferenceField(Challenges)
    scratch_card = ReferenceField(ScratchCards)
    

