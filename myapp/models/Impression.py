from mongoengine.document import Document
from mongoengine.fields import StringField, IntField


class Impression(Document):
	imdescription = StringField()
	showpiority = IntField()
	meta = {
		'ordering': ['-published_date']
	}
