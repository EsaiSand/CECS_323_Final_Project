from mongoengine import *

class Major(Document):
  # ---- Major attributes ----
  name = StringField(db_field='name', max_length=15, min_length=3, required=True)
  description = StringField(db_field='description', max_length=80, min_length=10, required=True)
  
  # ---- Embedded attributes ----
  deptAbbreviation = StringField(db_field='department_abbreviation', max_length=10, min_length=2, required=True)

  # Enforcing uniqueness constraints
  #  - No majors with same name
  meta = {'collection': 'majors',
          'indexes': [{'unique': True, 'fields': ['majorName'], 'name': 'majors_uk_01'}]
          }
  # Majors do not 'know' of associated students. 
  # Only know department abbreviation (retrieved from department collection on major creation)


  def __init__(self, name: str, description: str, deptAbbreviation: str, *args, **values):
    super().__init__(*args, **values)
    self.description = description
    self.name = name
    self.deptAbbreviation = deptAbbreviation

  def __str__(self):
    return f"{self.name} major:\n{self.description}\n"
