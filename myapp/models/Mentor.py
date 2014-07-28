from datetime import datetime

from mongoengine.django.auth import User
from mongoengine.document import Document
from mongoengine.fields import ReferenceField, DateTimeField


class Mentor(Document):
	published_date = DateTimeField(default=datetime.now)
	user = ReferenceField(User)
	meta = {
		'ordering': ['-published_date']
	}
