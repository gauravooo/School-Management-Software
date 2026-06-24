from app.db.base import Base
from app.db.session import engine
from app.models.user import User
from app.models.student import Student
from app.models.teacher import Teacher
from app.models.classroom import Classroom
from app.models.fee import FeePlan, FeePayment
from app.models.attendance import AttendanceRecord
from app.models.timetable import TimetableSlot
from app.models.notification import Notification


def init_db() -> None:
    Base.metadata.create_all(bind=engine)
