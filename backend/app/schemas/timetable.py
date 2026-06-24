from pydantic import BaseModel
from datetime import time

class TimetableSlotBase(BaseModel):
    classroom_id: int
    teacher_id: int
    subject: str
    day_of_week: str
    start_time: time
    end_time: time
    term: str | None = None

class TimetableSlotCreate(TimetableSlotBase):
    pass

class TimetableSlotRead(TimetableSlotBase):
    id: int

    class Config:
        from_attributes = True
