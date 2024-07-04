from mongoengine import *
import mongoengine

class Department(Document):
  # ---- Department attributes ----
  name = StringField(db_field='name', max_length=50, min_length=10, required=True)
  abbreviation = StringField(db_field='abbreviation', max_length=10, min_length=2, required=True)
  chair = StringField(db_field='chair', max_length=50, min_length=5, required=True)
  building = StringField(db_field='building', max_length=50, min_length=10, required=True)
  office = IntField(db_field='office', min_value=0, required=True)
  description = StringField(db_field='description', max_length=80, min_length=10, required=True)


  # ---- Relationship References ----
  # Reference to department majors, no embedding. When associated major deleted, remove from this list.
  majors = ListField(ReferenceField('Major'), reverse_delete_rule=mongoengine.PULL)
  # Reference to department courses, no embedding. When associated course deleted, remove from this list.
  courses = ListField(ReferenceField('Course'), reverse_delete_rule=mongoengine.PULL)

  # Enforcing uniqueness constraints
  #  - No depts with same name
  #  - No depts with same abbreviation
  #  - No depts with same chair
  #  - No depts with same building and office
  meta = {'collection': 'departments',
          'indexes': [{'unique': True, 'fields': ['name'], 'name': 'departments_uk_01'},
                      {'unique': True, 'fields': ['abbreviation'], 'name': 'departments_uk_02'},
                      {'unique': True, 'fields': ['chair'], 'name': 'departments_uk_03'},
                      {'unique': True, 'fields': ['building', 'office'], 'name': 'departments_uk_04'},]
          }
  
  def __init__(self, name: str, abbreviation: str, chair: str, building: str, office: int, description: str, *args, **values):
    super().__init__(*args, **values)
    self.name = name
    self.abbreviation = abbreviation
    self.chair = chair
    self.building = building
    self.office = office
    self.description = description

  def __str__(self):
    return f"{self.name} department({self.abbreviation}):\n\tChair: {self.chair}\n\tOffice: {self.building} {self.office}\n\tDescription: {self.description}" 


