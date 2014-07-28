'''
Created on Apr 3, 2014

@author: TuanNA
'''
from datetime import datetime

from mongoengine.django.auth import User
from mongoengine.document import Document
from mongoengine.fields import ReferenceField, StringField, DateTimeField,FileField


class UserProfile(Document):
	user_id = ReferenceField(User)
	job_title = StringField()
	images = StringField()
	company = StringField()
	work_field = StringField()
	edu = StringField()
	skill =StringField()
	create_date = DateTimeField(default=datetime.now)
	status = int()
	about = StringField()
	fileImage = FileField()
	meta = {
			'ordering': ['-create_date']
			}
