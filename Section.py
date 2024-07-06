from mongoengine import *
import mongoengine
from datetime import datetime
# from Course import Course

class Section(Document):
  # ---- Section Attributes ----
  sectionNumber = IntField(db_field='section_number', min_value=1, required=True)
  semester = StringField(db_field='semester', required = True)
  year = IntField(db_field='year', min_value=1984, required=True)
  building = StringField(db_field='building', required = True)
  room = IntField(db_field='room', min_value=1, required=True)
  schedule = StringField(db_field='schedule', required = True)
  startTime = DateTimeField(db_field='start_time', required=True)
  instructor = StringField(db_field='instructor', min_length=1, max_length=30, required = True)

  # ---- Embedded Attributes ----
  deptAbbreviation = StringField(db_field='department_abbreviation', required=True)
  courseNumber = StringField(db_field='course_number', required=True)

  # ---- Relationship References ----
  course = ReferenceField('Course', required=True) # Enforcing course delete rule in main to avoid circular rules

  # Enforcing Uniqueness Constraints
  #  - No two sections of a particular course with same section number within same semester 
  #  - No two sections in same semester with same schedule start at the same time, in the same room
  #  - No two sections in same semester with same schedule starting at the same time can have same instructor
  meta = {'collection': 'sections',
          'indexes': [{'unique': True, 'fields': ['sectionNumber', 'semester', 'year', 'course'], 'name': 'sections_uk_01'},
                      {'unique': True, 'fields': ['semester', 'year', 'building', 'room', 'startTime', 'schedule'], 'name': 'sections_uk_02'},
                      {'unique': True, 'fields': ['semester', 'year', 'startTime', 'instructor', 'schedule'], 'name': 'sections_uk_03'}]}


  def __init__(self, sectionNumber: int, semester: str, year: int, building: str, room: int, schedule: str, startTime: datetime, instructor: str, course, *args, **values):
    super().__init__(*args, **values)
    self.sectionNumber = sectionNumber
    self.semester = semester
    self.year = year
    self.building = building
    self.room = room
    self.schedule = schedule
    self.startTime = startTime
    self.instructor = instructor

    self.course = course
    self.deptAbbreviation = course.deptAbbreviation
    self.courseNumber = course.number

  def __str__(self):
    return f"{self.deptAbbreviation} {self.courseNumber} Sec {self.sectionNumber}: Starts {self.startTime} {self.schedule}, {self.semester} {self.year}"
