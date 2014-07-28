'''
Created on Apr 3, 2014

@author: TuanNA
'''
from mongoengine.django.auth import User
from mongoengine.document import Document
from mongoengine.fields import StringField, DateTimeField, ReferenceField


class UserChat(Document):
	message = StringField()
	published_date = DateTimeField()
	from_user = ReferenceField(User)
	to_user = ReferenceField(User)
	meta = {
		'ordering': ['-published_date']
	}
