'''
Created on Apr 3, 2014

@author: TuanNA
'''
from mongoengine.document import Document
from mongoengine.fields import StringField

class Social(Document):
	name=StringField()
	type=StringField(max_length=2)
	status=StringField(default=1)
	icon=StringField()
	link=StringField()
	meta = {
			'ordering': ['-name']
			}