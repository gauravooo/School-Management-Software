from fastapi import APIRouter
from app.api.api_v1.endpoints import users, classrooms, students, teachers, attendance, fees, timetable, notifications

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(classrooms.router, prefix="/classrooms", tags=["classrooms"])
api_router.include_router(students.router, prefix="/students", tags=["students"])
api_router.include_router(teachers.router, prefix="/teachers", tags=["teachers"])
api_router.include_router(attendance.router, prefix="/attendance", tags=["attendance"])
api_router.include_router(fees.router, prefix="/fees", tags=["fees"])
api_router.include_router(timetable.router, prefix="/timetable", tags=["timetable"])
api_router.include_router(notifications.router, prefix="/notifications", tags=["notifications"])
