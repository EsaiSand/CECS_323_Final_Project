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
