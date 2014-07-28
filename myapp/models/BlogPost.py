'''
Created on Apr 3, 2014

@author: TuanNA
'''
from mongoengine.django.auth import User
from mongoengine.document import Document
from mongoengine.fields import StringField, DateTimeField, ReferenceField


class BlogPost(Document):
	title = StringField()
	published_date = DateTimeField()
	user_id = ReferenceField(User)

	meta = {
		'ordering': ['-published_date']
	}
