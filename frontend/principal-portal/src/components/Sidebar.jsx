import React from 'react';
import { NavLink, useNavigate } from 'react-router-dom';
import { removeToken } from '../../shared/authUtils';
import './Sidebar.css';

function Sidebar() {
  const navigate = useNavigate();

  const handleLogout = () => {
    removeToken();
    navigate('/login');
  };

  return (
    <div className="sidebar">
      <h3>Principal Portal</h3>
      <nav>
        <NavLink to="/dashboard" className={({ isActive }) => isActive ? 'active' : ''}>
          Dashboard
        </NavLink>
        <NavLink to="/students" className={({ isActive }) => isActive ? 'active' : ''}>
          Students
        </NavLink>
        <NavLink to="/teachers" className={({ isActive }) => isActive ? 'active' : ''}>
          Teachers
        </NavLink>
        <NavLink to="/fees" className={({ isActive }) => isActive ? 'active' : ''}>
          Fee Management
        </NavLink>
        <NavLink to="/attendance" className={({ isActive }) => isActive ? 'active' : ''}>
          Attendance
        </NavLink>
        <NavLink to="/timetable" className={({ isActive }) => isActive ? 'active' : ''}>
          Timetable
        </NavLink>
        <NavLink to="/notifications" className={({ isActive }) => isActive ? 'active' : ''}>
          Notifications
        </NavLink>
      </nav>
      <button onClick={handleLogout} className="logout-btn">Logout</button>
    </div>
  );
}

export default Sidebar;
