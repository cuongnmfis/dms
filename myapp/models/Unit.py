from datetime import datetime

from mongoengine.document import Document
from mongoengine.fields import DateTimeField, StringField


class Unit(Document):
	published_date = DateTimeField(default=datetime.now)
	name = StringField()
	meta = {
		'ordering': ['-published_date']
	}
