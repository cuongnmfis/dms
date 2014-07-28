from datetime import datetime

from mongoengine.document import Document
from mongoengine.fields import StringField, ReferenceField, ListField, \
	DateTimeField

from myapp.models.Comment import Comment
from myapp.models.Statistic import Statistic


class Action(Document):
	published_date = DateTimeField(default=datetime.now)
	name = StringField()
	description = StringField()
	comment = ListField(ReferenceField(Comment))
	statistic = ReferenceField(Statistic)
	meta = {
		'ordering': ['-published_date']
	}
