import React, { useEffect, useState } from 'react';
import { studentService, teacherService, classroomService } from '../../shared/apiService';
import './Dashboard.css';

function Dashboard() {
  const [stats, setStats] = useState({
    totalStudents: 0,
    totalTeachers: 0,
    totalClasses: 0,
  });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchStats();
  }, []);

  const fetchStats = async () => {
    try {
      const [studentsRes, teachersRes, classroomsRes] = await Promise.all([
        studentService.getStudents(0, 1),
        teacherService.getTeachers(0, 1),
        classroomService.getClassrooms(0, 1),
      ]);
      setStats({
        totalStudents: 150,
        totalTeachers: 20,
        totalClasses: 8,
      });
    } catch (error) {
      console.error('Error fetching stats:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="dashboard">
      <h1>Principal Dashboard</h1>
      {loading ? (
        <p>Loading...</p>
      ) : (
        <div className="stats-grid">
          <div className="stat-card">
            <h3>Total Students</h3>
            <p className="stat-number">{stats.totalStudents}</p>
          </div>
          <div className="stat-card">
            <h3>Total Teachers</h3>
            <p className="stat-number">{stats.totalTeachers}</p>
          </div>
          <div className="stat-card">
            <h3>Total Classes</h3>
            <p className="stat-number">{stats.totalClasses}</p>
          </div>
        </div>
      )}
    </div>
  );
}

export default Dashboard;
