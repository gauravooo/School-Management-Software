# School Management System

Centralized school management platform with a FastAPI backend and React frontends for principals and teachers.

## Project Structure

- `backend/` — FastAPI REST API with PostgreSQL database
- `frontend/shared/` — Shared authentication and API service utilities
- `frontend/principal-portal/` — React app for principal dashboards
- `frontend/teacher-portal/` — React app for teacher dashboards

## Features

- **Centralized Database** — Students, teachers, classes, fees, attendance, timetable, marks, notifications
- **User Authentication** — JWT-based login with role-based access (principal, teacher)
- **Principal Dashboard** — Student/teacher management, fee tracking, attendance reports, timetable planning
- **Teacher Dashboard** — Class roster, attendance marking, marks entry, timetable view, teaching kit
- **Notifications** — System-wide announcements and notifications
- **API-First Architecture** — RESTful APIs for all core modules

## Setup

### Backend

1. Navigate to backend directory:
   ```bash
   cd backend
   ```

2. Create and activate virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run with uvicorn:
   ```bash
   uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
   ```

API docs available at `http://localhost:8000/docs`

### Frontend - Principal Portal

1. Navigate to principal portal directory:
   ```bash
   cd frontend/principal-portal
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start development server:
   ```bash
   npm start
   ```

Opens at `http://localhost:3000`

### Frontend - Teacher Portal

1. Navigate to teacher portal directory:
   ```bash
   cd frontend/teacher-portal
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start development server:
   ```bash
   npm start
   ```

Opens at `http://localhost:3001` (or next available port)

## API Endpoints

- `/api/v1/users` — Authentication (register, login)
- `/api/v1/students` — Student CRUD
- `/api/v1/teachers` — Teacher CRUD
- `/api/v1/classrooms` — Classroom CRUD
- `/api/v1/attendance` — Attendance records
- `/api/v1/fees` — Fee plans and payments
- `/api/v1/timetable` — Timetable slots
- `/api/v1/notifications` — Notifications and announcements

## Database Models

- **User** — Login credentials and roles (principal, teacher)
- **Student** — Student information with class assignment
- **Teacher** — Teacher data with subject assignment
- **Classroom** — Class and section information
- **AttendanceRecord** — Daily attendance tracking
- **FeePlan** — Fee structure per class
- **FeePayment** — Student fee payment records
- **TimetableSlot** — Schedule for classes
- **Notification** — System announcements

## Development Notes

- Backend uses PostgreSQL (via SQLite for development)
- Frontend uses React with React Router for navigation
- Authentication uses JWT tokens stored in localStorage
- All API calls are intercepted to add authorization headers

## Phase 2 Enhancements

- [ ] Parent portal for viewing student progress
- [ ] Student portal for accessing own marks and attendance
- [ ] Mobile-friendly responsive design
- [ ] Advanced reporting and analytics
- [ ] Exam scheduling and result management
- [ ] Payment gateway integration
