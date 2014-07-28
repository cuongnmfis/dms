from datetime import datetime

from mongoengine.django.auth import User
from mongoengine.document import Document
from mongoengine.fields import  DateTimeField, ReferenceField, IntField

from myapp.models.Material import Material


class MaterialLog(Document):
	published_date = DateTimeField(default=datetime.now)
	material = ReferenceField(Material)
	Like = IntField()
	user = ReferenceField(User)
	meta = {
			'ordering': ['-published_date']
 }
