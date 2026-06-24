@echo off
REM Development startup script for Windows

echo Starting School Management System...
echo.

REM Start backend
echo Starting FastAPI backend...
cd backend
if not exist .venv (
    python -m venv .venv
)
call .venv\Scripts\Activate.ps1
pip install -r requirements.txt
start "SMS Backend" uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
echo Backend started

REM Wait a bit
timeout /t 3 /nobreak

REM Start principal portal
echo Starting Principal Portal...
cd ..\frontend\principal-portal
if not exist node_modules (
    call npm install
)
start "SMS Principal Portal" npm start
echo Principal Portal started

REM Start teacher portal  
echo Starting Teacher Portal...
cd ..\teacher-portal
if not exist node_modules (
    call npm install
)
start "SMS Teacher Portal" npm start
echo Teacher Portal started

echo.
echo =========================================
echo All services started successfully!
echo Backend API: http://localhost:8000
echo API Docs: http://localhost:8000/docs
echo Principal Portal: http://localhost:3000
echo Teacher Portal: http://localhost:3001
echo =========================================
echo.
pause
