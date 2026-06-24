import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { isAuthenticated } from '../shared/authUtils';
import Login from '../shared/Login';
import TeacherDashboard from './pages/Dashboard';
import MyClasses from './pages/MyClasses';
import AttendanceMarking from './pages/AttendanceMarking';
import MarksEntry from './pages/MarksEntry';
import TeacherTimetable from './pages/Timetable';
import TeacherNotifications from './pages/Notifications';
import TeachingResources from './pages/TeachingResources';
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
                    <Route path="/dashboard" element={<TeacherDashboard />} />
                    <Route path="/classes" element={<MyClasses />} />
                    <Route path="/attendance" element={<AttendanceMarking />} />
                    <Route path="/marks" element={<MarksEntry />} />
                    <Route path="/timetable" element={<TeacherTimetable />} />
                    <Route path="/notifications" element={<TeacherNotifications />} />
                    <Route path="/resources" element={<TeachingResources />} />
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
