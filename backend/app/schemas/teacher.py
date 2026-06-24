from pydantic import BaseModel
from typing import Optional

class TeacherBase(BaseModel):
    first_name: str
    last_name: str
    employee_id: str
    subject: Optional[str] = None
    email: str
    phone_number: Optional[str] = None

class TeacherCreate(TeacherBase):
    pass

class TeacherRead(TeacherBase):
    id: int

    class Config:
        from_attributes = True
