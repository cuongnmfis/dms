'''
Created on Apr 3, 2014

@author: TuanNA
'''
from datetime import datetime

from mongoengine.django.auth import User
from mongoengine.document import Document
from mongoengine.fields import ReferenceField, DateTimeField, IntField
class RatingPost(Document):
	create_date = DateTimeField(default=datetime.now)
	user_id = ReferenceField(User)
	starnumber = IntField()
	meta = {
			'ordering': ['-published_date']
 }