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
      <h3>Teacher Portal</h3>
      <nav>
        <NavLink to="/dashboard" className={({ isActive }) => isActive ? 'active' : ''}>
          Dashboard
        </NavLink>
        <NavLink to="/classes" className={({ isActive }) => isActive ? 'active' : ''}>
          My Classes
        </NavLink>
        <NavLink to="/attendance" className={({ isActive }) => isActive ? 'active' : ''}>
          Attendance
        </NavLink>
        <NavLink to="/marks" className={({ isActive }) => isActive ? 'active' : ''}>
          Marks Entry
        </NavLink>
        <NavLink to="/timetable" className={({ isActive }) => isActive ? 'active' : ''}>
          My Timetable
        </NavLink>
        <NavLink to="/notifications" className={({ isActive }) => isActive ? 'active' : ''}>
          Notifications
        </NavLink>
        <NavLink to="/resources" className={({ isActive }) => isActive ? 'active' : ''}>
          Teaching Kit
        </NavLink>
      </nav>
      <button onClick={handleLogout} className="logout-btn">Logout</button>
    </div>
  );
}

export default Sidebar;
