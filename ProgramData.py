from datetime import datetime

VALIDS = {
  'semesters': ['Fall', 'Winter', 'Spring', 'Summer I', 'Summer II'],
  'buildings': ['VEC', 'ECS', 'EN2', 'EN3', 'EN4', 'ET', 'SSPA'],
  'schedules': ['MW', 'TuTh', 'MWF', 'F', 'S']
}

BUIDLINGS = 'buildings'
SEMESTERS = 'semesters'
SCHEDULES = 'schedules'

REFERENCE_DATE = datetime.today()
CURRENT_SEMESTER = ''

def change_ref_date(new_date: datetime):
  REFERENCE_DATE = new_date
  update_semester(REFERENCE_DATE)

def update_semester(reference_date: datetime):
  
  pass