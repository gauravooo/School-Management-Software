from pydantic import BaseModel
from datetime import datetime

class NotificationBase(BaseModel):
    title: str
    message: str
    owner_id: int | None = None
    is_broadcast: bool = False

class NotificationCreate(NotificationBase):
    pass

class NotificationRead(NotificationBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
