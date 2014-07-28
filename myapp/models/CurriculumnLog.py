from datetime import datetime

from mongoengine.django.auth import User
from mongoengine.document import Document
from mongoengine.fields import  DateTimeField, ReferenceField, IntField, \
	StringField

from myapp.models.Curriculumn import Curriculumn
from myapp.models.ProgressType import ProgressType


class CurriculumnLog(Document):
	published_date = DateTimeField(default=datetime.now)
	curriculumn = ReferenceField(Curriculumn)
	process =ReferenceField(ProgressType)
	user_id = ReferenceField('User')
	data = StringField()
	lastUpdate=DateTimeField(default=datetime.now)
	meta = {
			'ordering': ['-published_date']
}
