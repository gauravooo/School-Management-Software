import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { isAuthenticated } from '../shared/authUtils';
import Login from '../shared/Login';
import PrincipalDashboard from './pages/Dashboard';
import StudentManagement from './pages/StudentManagement';
import TeacherManagement from './pages/TeacherManagement';
import FeeManagement from './pages/FeeManagement';
import AttendanceOverview from './pages/AttendanceOverview';
import Timetable from './pages/Timetable';
import Notifications from './pages/Notifications';
import Sidebar from './components/Sidebar';
import './App.css';

const ProtectedRoute = ({ children }) => {
  return isAuthenticated() ? children : <Navigate to="/login" />;
};

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route
          path="/*"
          element={
            <ProtectedRoute>
              <div className="app-layout">
                <Sidebar />
                <div className="main-content">
                  <Routes>
                    <Route path="/dashboard" element={<PrincipalDashboard />} />
                    <Route path="/students" element={<StudentManagement />} />
                    <Route path="/teachers" element={<TeacherManagement />} />
                    <Route path="/fees" element={<FeeManagement />} />
                    <Route path="/attendance" element={<AttendanceOverview />} />
                    <Route path="/timetable" element={<Timetable />} />
                    <Route path="/notifications" element={<Notifications />} />
                    <Route path="/" element={<Navigate to="/dashboard" />} />
                  </Routes>
                </div>
              </div>
            </ProtectedRoute>
          }
        />
      </Routes>
    </Router>
  );
}

export default App;
