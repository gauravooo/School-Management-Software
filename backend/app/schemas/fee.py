from pydantic import BaseModel
from datetime import date
from decimal import Decimal

class FeePlanBase(BaseModel):
    class_id: int
    amount: Decimal
    due_date: date | None = None
    description: str | None = None

class FeePlanCreate(FeePlanBase):
    pass

class FeePlanRead(FeePlanBase):
    id: int

    class Config:
        orm_mode = True

class FeePaymentBase(BaseModel):
    student_id: int
    fee_plan_id: int
    amount_paid: Decimal
    payment_date: date
    paid: bool = True

class FeePaymentCreate(FeePaymentBase):
    pass

class FeePaymentRead(FeePaymentBase):
    id: int

    class Config:
        from_attributes = True
