from mongoengine import *
from Section import Section

class Course(Document):
  # ---- Course Attributes ----
  name = StringField(db_field='name', min_length=5, max_length=60, required=True)
  number = IntField(db_field='number', min_value=100, max_value=599, required=True)
  description = StringField(db_field='description', min_length=10, max_length=600, required=True)
  units = IntField(db_field='units', min_value=1, max_value=5, required=True)

  # ---- Embeddeed Attributes ----
  deptAbbreviation = StringField(db_field='course_department', required=True)
  currentSections = EmbeddedDocumentListField(Section, db_field='current_sections')

  def __init__(self, name: str, number: int, description: str, units: int, deptAbbreviation: str,*args, **values):
    super().__init__(*args, **values)
    self.name = name
    self.number = number
    self.description = description
    self.units = units
    self.deptAbbreviation = deptAbbreviation

  def __str__(self):
    return 
