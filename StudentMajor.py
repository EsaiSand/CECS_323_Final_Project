from mongoengine import *
from datetime import datetime

class StudentMajor(EmbeddedDocument):
  majorName = StringField(db_field='major', required=True)
  declarationDate = DateTimeField(db_field='declaration_date', required=True)

  def __init__(self, majorName: str, declarationDate: datetime, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.majorName = majorName
    self.declarationDate = declarationDate

  def __str__(self):
    return f"{self.majorName} major declared {self.declarationDate}"