'''
Created on Apr 3, 2014

@author: TuanNA
'''
from datetime import datetime

from mongoengine.document import Document
from mongoengine.fields import StringField, DateTimeField,FloatField

class LoanType(Document):
	create_date = DateTimeField(default=datetime.now)
	code  = StringField()
	name = StringField()
	status = FloatField()
	description = StringField()
	unit = StringField()
	meta = {
			'ordering': ['-create_date']
			}