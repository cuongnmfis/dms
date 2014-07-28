from datetime import datetime
from mongoengine.django.auth import User
from mongoengine.document import Document
from mongoengine.fields import StringField, ReferenceField, DateTimeField


class StudyLog(Document):
	published_date = DateTimeField(default=datetime.now)
	data = StringField()
	user = ReferenceField(User)	
	meta = {
		'ordering': ['-published_date']
	}
