from pydantic import BaseModel
from datetime import date

class AttendanceBase(BaseModel):
    student_id: int
    class_id: int
    date: date
    present: bool

class AttendanceCreate(AttendanceBase):
    pass

class AttendanceRead(AttendanceBase):
    id: int

    class Config:
        from_attributes = True
