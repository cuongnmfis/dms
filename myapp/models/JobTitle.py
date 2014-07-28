'''
Created on Apr 3, 2014

@author: TuanNA
'''
from datetime import datetime

from mongoengine.document import Document
from mongoengine.fields import StringField, DateTimeField


class JobTitle(Document):
	code= StringField()
	name= StringField()
	create_date = DateTimeField(default=datetime.now)
	status = int()
