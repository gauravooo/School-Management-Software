from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.notification import NotificationCreate, NotificationRead
from app.db.session import get_db
from app.crud.notification import create_notification, get_notifications, get_notification
from app.api.dependencies import get_current_user

router = APIRouter()

@router.post("/", response_model=NotificationRead, dependencies=[Depends(get_current_user)])
def create_notification_endpoint(notification_in: NotificationCreate, db: Session = Depends(get_db)):
    return create_notification(db, notification_in)

@router.get("/", response_model=list[NotificationRead], dependencies=[Depends(get_current_user)])
def list_notifications(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_notifications(db, skip=skip, limit=limit)

@router.get("/{notification_id}", response_model=NotificationRead, dependencies=[Depends(get_current_user)])
def read_notification(notification_id: int, db: Session = Depends(get_db)):
    notification = get_notification(db, notification_id)
    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    return notification
