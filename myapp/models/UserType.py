'''
Created on Apr 3, 2014

@author: TuanNA
'''
from datetime import datetime

from mongoengine.document import Document
from mongoengine.fields import StringField, DateTimeField


class UserType(Document):
	code= StringField(max_length=1)
	user_type= StringField(max_length=15)
	name= StringField(max_length=15)
	create_date = DateTimeField(default=datetime.now)
	status = int()
	meta = {
			'ordering': ['-create_date']
 }
