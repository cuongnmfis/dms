from datetime import datetime

from mongoengine.document import Document
from mongoengine.fields import DateTimeField, ReferenceField, \
	StringField

from myapp.models.Action import Action
from myapp.models.Impression import Impression
from myapp.models.ProgressType import ProgressType
from myapp.models.Student import Student


class ActionStudyLog(Document):
	published_date = DateTimeField(default=datetime.now)
	action = ReferenceField(Action)
	student = ReferenceField(Student)
	impression = ReferenceField(Impression)	
	progressType = ReferenceField(ProgressType)
	description = StringField()	
	meta = {
			'ordering': ['-published_date']
 }
