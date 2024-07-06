from mongoengine import *
from datetime import datetime
from Major import Major
import mongoengine

class StudentMajor(EmbeddedDocument):
  # ---- Student Major attributes
  declarationDate = DateTimeField(db_field='declaration_date', required=True)

  # ---- Embedded Attributes ----
  majorName = StringField(db_field='declared_major', required=True)

  # ---- Reference Fields ----
  major = ReferenceField(Major, required=True, reverse_delete_rule=mongoengine.DENY)

  def __init__(self, majorName: str, declarationDate: datetime, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.majorName = majorName
    self.declarationDate = declarationDate

  def __str__(self):
    return f"{self.majorName} major declared {self.declarationDate}"