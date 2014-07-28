'''
Created on Apr 3, 2014

@author: TuanNA
'''
from mongoengine.document import Document
from mongoengine.fields import ReferenceField,StringField,\
	ListField

from myapp.models.CommentPost import CommentPost


class Esay(Document):
	title = StringField()
	content = StringField()
	comments = ListField(ReferenceField(CommentPost))
	meta = {
			'ordering': ['-published_date']
 }