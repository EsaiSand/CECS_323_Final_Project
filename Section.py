from mongoengine import *

class Section:
  sectionNumber = IntField(db_field='section_number')