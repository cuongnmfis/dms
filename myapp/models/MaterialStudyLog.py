from datetime import datetime

from mongoengine.document import Document
from mongoengine.fields import DateTimeField, ReferenceField, \
	StringField

from myapp.models.Impression import Impression
from myapp.models.Material import Material
from myapp.models.ProgressType import ProgressType
from myapp.models.Student import Student


class MaterialStudyLog(Document):
	published_date = DateTimeField(default=datetime.now)	
	
	material = ReferenceField(Material)
	student = ReferenceField(Student)
	impression = ReferenceField(Impression)	
	progressType = ReferenceField(ProgressType)
	description = StringField()	
	meta = {
			'ordering': ['-published_date']
 }
