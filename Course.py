from mongoengine import *
import mongoengine
from Section import Section
from Department import Department

class Course(Document):
  # ---- Course Attributes ----
  name = StringField(db_field='name', min_length=5, max_length=60, required=True)
  number = IntField(db_field='number', min_value=100, max_value=599, required=True)
  description = StringField(db_field='description', min_length=10, max_length=600, required=True)
  units = IntField(db_field='units', min_value=1, max_value=5, required=True)

  # ---- Embeddeed Attributes ----
  deptAbbreviation = StringField(db_field='course_department', required=True)

  # --- Relationship Attributes
  department = ReferenceField(Department, required=True, reverse_delete_rule=mongoengine.DENY)

  # Enforcing Uniqueness Constraints
  # - No two courses with same name
  # - No two courses within same department with same number
  # - No two courses with same description
  meta = {'collection': 'courses',
          'indexes': [{'unique': True, 'fields': ['name'], 'name': 'courses_uk_01'},
                      {'unique': True, 'fields': ['deptAbbreviation', 'number'], 'name': 'courses_uk_02'},
                      {'unique': True, 'fields': ['description'], 'name': 'courses_uk_03'},]
          }

  def __init__(self, name: str, number: int, description: str, units: int, department: Department, deptAbbreviation: str,*args, **values):
    super().__init__(*args, **values)
    self.name = name
    self.number = number
    self.description = description
    self.units = units
    self.department = department
    self.deptAbbreviation = deptAbbreviation
  
  def equals(self, other_course):
    return self.name == other_course.name

  def __str__(self):
    return
  
