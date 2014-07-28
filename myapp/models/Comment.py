from datetime import datetime

from mongoengine.django.auth import User
from mongoengine.document import Document
from mongoengine.fields import ReferenceField, DateTimeField, StringField

class Comment(Document):
	create_date = DateTimeField(default=datetime.now)
	user = ReferenceField(User)
	content = StringField()
	status = StringField(default='1')
	meta = {
			'ordering': ['-published_date']
 }