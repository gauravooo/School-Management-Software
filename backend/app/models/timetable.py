from sqlalchemy import Column, Integer, ForeignKey, String, Time, Date
from sqlalchemy.orm import relationship
from app.db.base import Base

class TimetableSlot(Base):
    __tablename__ = "timetable_slots"

    id = Column(Integer, primary_key=True, index=True)
    classroom_id = Column(Integer, ForeignKey("classrooms.id"), nullable=False)
    teacher_id = Column(Integer, ForeignKey("teachers.id"), nullable=False)
    subject = Column(String, nullable=False)
    day_of_week = Column(String, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    term = Column(String, nullable=True)

    classroom = relationship("Classroom", back_populates="timetable_slots")
    teacher = relationship("Teacher", back_populates="timetable_slots")
