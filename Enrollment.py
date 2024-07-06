"""
Malcolm Roddy
Mongo Enrollment final project

"""

from mongoengine import *
from datetime import datetime
from Student import Student
from Section import Section

class Enrollment(Document):
    """
    The association class between Student and Section
    """
    # Relationships 
    student = ReferenceField(Student, reverse_delete_rule = CASCADE)
    section = ReferenceField(Section, reverse_delete_rule = CASCADE)
    enrollmentDate = DateTimeField(required=True, default=datetime.now)

    meta = {
        'collection': 'enrollments',
        'indexes': [
            {'fields': ['student', 'section'], 'unique': True}
        ]
    }

    def __init__(self, student: Student, section: Section, enrollmentDate: datetime, *args, **kwargs):
        """
        Init enrollment by adding student and section 
        """
        super().__init__(*args, **kwargs)
        self.student = student
        self.section = section
        self.enrollmentDate = enrollmentDate

    def __str__(self):
        return f"Enrollment - Student: {self.student}, Section: {self.section}, Date: {self.enrollment_date}"
    
    
"""

Add delete functions
ToDo: move this into main for testing 

NOTE - add these imports 
from mongoengine import DoesNotExist
from datetime import datetime
Note - need to impoirt DoesNotExist from mongo engine to work 
checks if object id it matched by enrollment_id 

"""
def add_enrollment(studentId, sectionId):
    """
    Add an enrollment for a student in a section.
    """
    # Retrieve student and section objects
    print("Select student you wish to enroll")
    student = select_student()
    print("Select section you wish to enroll")
    section = select_section()
    
    # Create a new enrollment
    enrollment = Enrollment(student=student, section=section, enrollment_date=datetime.now())
    enrollment.save()
    print("Enrolled student success\n")
    
    return enrollment


def delete_enrollment(enrollmentId):
    """
    Delete an enrollment by its ObjectId 
    """
    try:
        enrollment = Enrollment.objects.get(id=enrollmentId)
        enrollment.delete()
        return True
    except DoesNotExist:
        print(f"Enrollment with id {enrollmentId} does not exist.")
        return False


def list_enrollments():
    enrollments = Enrollment.objects()
    for enrollment in enrollments:
        print(f"Enrollment ID: {enrollment.id}")
        print(f"Student: {enrollment.student.name}")
        print(f"Section: {enrollment.section.section_number}")
        print(f"Enrollment Date: {enrollment.enrollment_date}")
        print("---")
