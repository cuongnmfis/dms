'''
Created on Apr 3, 2014

@author: TuanNA
'''
from mongoengine.document import Document
from mongoengine.fields import StringField


class WorkField(Document):
	code= StringField(max_length=5)
	type_name = StringField()
	status = int()
