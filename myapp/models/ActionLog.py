from datetime import datetime

from mongoengine.django.auth import User
from mongoengine.document import Document
from mongoengine.fields import  DateTimeField, ReferenceField, IntField

from myapp.models.Action import Action


class ActionLog(Document):
	published_date = DateTimeField(default=datetime.now)
	action = ReferenceField(Action)
	like = IntField()
	user = ReferenceField(User)
	meta = {
			'ordering': ['-published_date']
 }
