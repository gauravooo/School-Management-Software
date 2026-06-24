#!/bin/bash
# Development startup script

echo "Starting School Management System..."

# Start backend
echo "Starting FastAPI backend..."
cd backend
python -m venv .venv
source .venv/bin/activate 2>/dev/null || .venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000 &
BACKEND_PID=$!
echo "Backend started with PID $BACKEND_PID"

# Wait a bit for backend to start
sleep 3

# Start principal portal
echo "Starting Principal Portal..."
cd ../frontend/principal-portal
npm install
npm start &
PRINCIPAL_PID=$!
echo "Principal Portal started with PID $PRINCIPAL_PID"

# Start teacher portal
echo "Starting Teacher Portal..."
cd ../teacher-portal
npm install
npm start &
TEACHER_PID=$!
echo "Teacher Portal started with PID $TEACHER_PID"

echo ""
echo "========================================="
echo "All services started successfully!"
echo "Backend API: http://localhost:8000"
echo "API Docs: http://localhost:8000/docs"
echo "Principal Portal: http://localhost:3000"
echo "Teacher Portal: http://localhost:3001"
echo "========================================="
echo ""
echo "Press Ctrl+C to stop all services"

# Wait for all processes
wait
