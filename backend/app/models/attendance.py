from sqlalchemy import Column, Integer, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base

class AttendanceRecord(Base):
    __tablename__ = "attendance_records"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    date = Column(Date, nullable=False)
    present = Column(Boolean, nullable=False)
    class_id = Column(Integer, ForeignKey("classrooms.id"), nullable=False)

    student = relationship("Student", back_populates="attendances")
    classroom = relationship("Classroom")
