from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.fee import FeePlanCreate, FeePlanRead, FeePaymentCreate, FeePaymentRead
from app.db.session import get_db
from app.crud.fee import (
    create_fee_plan,
    get_fee_plans,
    get_fee_plan,
    create_fee_payment,
    get_fee_payments,
    get_fee_payment,
)
from app.api.dependencies import get_current_user

router = APIRouter()

@router.post("/plans/", response_model=FeePlanRead, dependencies=[Depends(get_current_user)])
def create_fee_plan_endpoint(fee_plan_in: FeePlanCreate, db: Session = Depends(get_db)):
    return create_fee_plan(db, fee_plan_in)

@router.get("/plans/", response_model=list[FeePlanRead], dependencies=[Depends(get_current_user)])
def list_fee_plans(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_fee_plans(db, skip=skip, limit=limit)

@router.get("/plans/{fee_plan_id}", response_model=FeePlanRead, dependencies=[Depends(get_current_user)])
def read_fee_plan(fee_plan_id: int, db: Session = Depends(get_db)):
    fee_plan = get_fee_plan(db, fee_plan_id)
    if not fee_plan:
        raise HTTPException(status_code=404, detail="Fee plan not found")
    return fee_plan

@router.post("/payments/", response_model=FeePaymentRead, dependencies=[Depends(get_current_user)])
def create_fee_payment_endpoint(payment_in: FeePaymentCreate, db: Session = Depends(get_db)):
    return create_fee_payment(db, payment_in)

@router.get("/payments/", response_model=list[FeePaymentRead], dependencies=[Depends(get_current_user)])
def list_fee_payments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_fee_payments(db, skip=skip, limit=limit)

@router.get("/payments/{payment_id}", response_model=FeePaymentRead, dependencies=[Depends(get_current_user)])
def read_fee_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = get_fee_payment(db, payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Fee payment not found")
    return payment
