from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    roll_number = Column(String, unique=True, nullable=False, index=True)
    class_id = Column(Integer, ForeignKey("classrooms.id"), nullable=False)
    section = Column(String, nullable=True)
    enrollment_year = Column(Integer, nullable=True)
    parent_contact = Column(String, nullable=True)

    classroom = relationship("Classroom", back_populates="students")
    attendances = relationship("AttendanceRecord", back_populates="student")
    fee_payments = relationship("FeePayment", back_populates="student")
