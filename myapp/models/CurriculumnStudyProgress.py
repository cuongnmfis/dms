from datetime import datetime

from mongoengine.django.auth import User
from mongoengine.document import Document
from mongoengine.fields import DateTimeField, ReferenceField, \
	StringField

from myapp.models.Curriculumn import Curriculumn
from myapp.models.Impression import Impression
from myapp.models.ProgressType import ProgressType
from myapp.models.Student import Student


class CurriculumnStudyProgress(Document):
	published_date = DateTimeField(default=datetime.now)	
	curriculumn = ReferenceField('Curriculumn')
	student = ReferenceField('Student')
	impression = ReferenceField(Impression)	
	progressType = ReferenceField(ProgressType)	
	description = StringField()	
	PlanStartDate = DateTimeField()
	PlanEndDate = DateTimeField()
	ActualStartDate = DateTimeField()
	ActualEndDate = DateTimeField()
	lastUpdate = DateTimeField()
	meta = {
			'ordering': ['-published_date']
 }
