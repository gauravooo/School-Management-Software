from pydantic import BaseModel
from typing import Optional

class StudentBase(BaseModel):
    first_name: str
    last_name: str
    roll_number: str
    class_id: int
    section: Optional[str] = None
    enrollment_year: Optional[int] = None
    parent_contact: Optional[str] = None

class StudentCreate(StudentBase):
    pass

class StudentRead(StudentBase):
    id: int

    class Config:
        from_attributes = True
