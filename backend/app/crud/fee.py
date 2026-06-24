from sqlalchemy.orm import Session
from app.models.fee import FeePlan, FeePayment
from app.schemas.fee import FeePlanCreate, FeePaymentCreate


def get_fee_plan(db: Session, fee_plan_id: int) -> FeePlan | None:
    return db.query(FeePlan).filter(FeePlan.id == fee_plan_id).first()


def get_fee_plans(db: Session, skip: int = 0, limit: int = 100):
    return db.query(FeePlan).offset(skip).limit(limit).all()


def create_fee_plan(db: Session, fee_plan_in: FeePlanCreate) -> FeePlan:
    fee_plan = FeePlan(**fee_plan_in.dict())
    db.add(fee_plan)
    db.commit()
    db.refresh(fee_plan)
    return fee_plan


def get_fee_payment(db: Session, payment_id: int) -> FeePayment | None:
    return db.query(FeePayment).filter(FeePayment.id == payment_id).first()


def get_fee_payments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(FeePayment).offset(skip).limit(limit).all()


def create_fee_payment(db: Session, payment_in: FeePaymentCreate) -> FeePayment:
    payment = FeePayment(**payment_in.dict())
    db.add(payment)
    db.commit()
    db.refresh(payment)
    return payment
