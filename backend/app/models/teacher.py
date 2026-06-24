from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    employee_id = Column(String, unique=True, nullable=False, index=True)
    subject = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=False)
    phone_number = Column(String, nullable=True)

    timetable_slots = relationship("TimetableSlot", back_populates="teacher")
