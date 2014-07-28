from datetime import datetime

from mongoengine.document import Document
from mongoengine.fields import StringField, DateTimeField, ReferenceField, \
	ListField

from myapp.models.Comment import Comment
from myapp.models.MaterialType import MaterialType
from myapp.models.Statistic import Statistic
from myapp.models.Unit import Unit


class Material(Document):
	published_date = DateTimeField(default=datetime.now)
	unit = ReferenceField(Unit)
	type = ReferenceField(MaterialType)
	name = StringField()
	url = StringField()
	code = StringField()
	description = StringField()
	comment = ListField(ReferenceField(Comment))
	statistic = ReferenceField(Statistic)
	note = StringField(default='0')
	meta = {
			'ordering': ['-published_date']
 }