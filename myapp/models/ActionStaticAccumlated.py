from datetime import datetime

from mongoengine.document import Document
from mongoengine.fields import  DateTimeField, ReferenceField, IntField

from myapp.models.Action import Action


class ActionStaticAccumlated(Document):
	published_date = DateTimeField(default=datetime.now)
	action = ReferenceField(Action)
	currentLikeNumber = IntField()
	currentTakenNumber = IntField()
	lastUpdate = DateTimeField()
	meta = {
			'ordering': ['-published_date']
 }
