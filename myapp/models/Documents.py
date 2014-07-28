'''
Created on Apr 3, 2014

@author: TuanNA
'''
from mongoengine.document import Document
from mongoengine.fields import FileField


class Documents(Document):
	doc_file = FileField()
