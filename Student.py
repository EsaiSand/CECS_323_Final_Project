from mongoengine import *
import mongoengine
from StudentMajor import StudentMajor

class Student(Document):
  # ---- Student attributes ----
  lastName = StringField(db_field='last_name', max_length=30, min_length=1, required=True)
  firstName = StringField(db_field='first_name', max_length=30, min_length=1, required=True)
  email = StringField(db_field='email', max_length=50, min_length=5, required=True)

  # ---- Embedded attributes ----
  majors = EmbeddedDocumentListField(StudentMajor, db_field='student_majors')

  # Enforcing uniqueness constraints:
  #  - No students with same email
  meta = {'collection': 'students',
          'indexes': [{'unique': True, 'fields': ['email'], 'name': 'students_uk_01'}]}
  
  def __init__(self, lastName: str, firstName: str, email: str, *args, **values):
    super().__init__(*args, **values)
    self.lastName = lastName
    self.firstName = firstName
    self.email = email

  def __str__(self):
    return f"{self.firstName} {self.lastName}, {self.email}"
  
