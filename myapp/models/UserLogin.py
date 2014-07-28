'''
Created on Apr 3, 2014

@author: TuanNA
'''
from datetime import datetime

from mongoengine.django.auth import User
from mongoengine.document import Document
from mongoengine.fields import DateTimeField, ReferenceField


class UserLogin(Document):
	published_date = DateTimeField(default=datetime.now)
	use = ReferenceField(User)
	meta = {
		'ordering': ['-published_date']
	}
