from sqlalchemy.orm import Session
from app.models.notification import Notification
from app.schemas.notification import NotificationCreate


def get_notification(db: Session, notification_id: int) -> Notification | None:
    return db.query(Notification).filter(Notification.id == notification_id).first()


def get_notifications(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Notification).offset(skip).limit(limit).all()


def create_notification(db: Session, notification_in: NotificationCreate) -> Notification:
    notification = Notification(**notification_in.dict())
    db.add(notification)
    db.commit()
    db.refresh(notification)
    return notification
