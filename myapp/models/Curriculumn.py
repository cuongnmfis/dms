from datetime import datetime

from mongoengine.django.auth import User
from mongoengine.document import Document
from mongoengine.fields import StringField, DateTimeField, ReferenceField, IntField, \
	ListField

from myapp.models.Action import Action
from myapp.models.Category import Category
from myapp.models.Comment import Comment
from myapp.models.Material import Material
from myapp.models.Mentor import Mentor
from myapp.models.Statistic import Statistic
from myapp.models.Unit import Unit


class Curriculumn(Document):
	published_date = DateTimeField(default=datetime.now)
	name = StringField()
	duration = IntField()
	duration_type = StringField()
	category= ReferenceField(Category)
	from_date = DateTimeField(default=datetime.now)
	to_date = DateTimeField(default=datetime.now)
	description = StringField()
	mentor = ReferenceField(Mentor)
	units = ListField(ReferenceField(Unit))
	comments = ListField(ReferenceField(Comment))
	material = ListField(ReferenceField(Material))
	action = ListField(ReferenceField(Action))
	statistic = ReferenceField(Statistic)
	joined_user = ListField(ReferenceField(User))
	meta = {
				'ordering': ['-mentor'],
				'ordering': ['-comments'],
				'ordering': ['-units']
			}
