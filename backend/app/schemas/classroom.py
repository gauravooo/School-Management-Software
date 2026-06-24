from pydantic import BaseModel

class ClassroomBase(BaseModel):
    name: str
    grade: str
    section: str

class ClassroomCreate(ClassroomBase):
    pass

class ClassroomRead(ClassroomBase):
    id: int

    class Config:
        from_attributes = True
