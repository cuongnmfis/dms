'''
Created on Apr 3, 2014

@author: TuanNA
'''
from mongoengine.django.auth import User
from mongoengine.document import Document
from mongoengine.fields import StringField,ReferenceField

from myapp.models.Social import Social
class SocialProfile(Document):
	name=StringField()
	user_id=ReferenceField(User)
	social_id=ReferenceField(Social)
	link=StringField()
	status=StringField()
	meta = {
		'ordering': ['-user_id']
		}