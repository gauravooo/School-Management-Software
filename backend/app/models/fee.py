from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, Date, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base

class FeePlan(Base):
    __tablename__ = "fee_plans"

    id = Column(Integer, primary_key=True, index=True)
    class_id = Column(Integer, ForeignKey("classrooms.id"), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    due_date = Column(Date, nullable=True)
    description = Column(String, nullable=True)

    classroom = relationship("Classroom")
    payments = relationship("FeePayment", back_populates="fee_plan")

class FeePayment(Base):
    __tablename__ = "fee_payments"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    fee_plan_id = Column(Integer, ForeignKey("fee_plans.id"), nullable=False)
    amount_paid = Column(Numeric(10, 2), nullable=False)
    payment_date = Column(Date, nullable=False)
    paid = Column(Boolean, default=True)

    student = relationship("Student", back_populates="fee_payments")
    fee_plan = relationship("FeePlan", back_populates="payments")
