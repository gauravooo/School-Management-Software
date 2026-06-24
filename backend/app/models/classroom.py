from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class Classroom(Base):
    __tablename__ = "classrooms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    grade = Column(String, nullable=False)
    section = Column(String, nullable=True)

    students = relationship("Student", back_populates="classroom")
    timetable_slots = relationship("TimetableSlot", back_populates="classroom")
