from mongoengine.document import Document
from mongoengine.fields import StringField, ReferenceField, IntField

class Category(Document):
	categoryName = StringField()
	parentCategory = ReferenceField('Category')
	currentCategoryTree = StringField()
	showpiority = IntField()
	isparent = StringField()
	meta = {
	}