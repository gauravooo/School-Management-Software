import React, { useEffect, useState } from 'react';
import { classroomService } from '../../shared/apiService';
import './Dashboard.css';

function Dashboard() {
  const [stats, setStats] = useState({
    myClasses: 0,
    totalStudents: 0,
  });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchStats();
  }, []);

  const fetchStats = async () => {
    try {
      const response = await classroomService.getClassrooms(0, 100);
      setStats({
        myClasses: response.data.length,
        totalStudents: 45,
      });
    } catch (error) {
      console.error('Error fetching stats:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="dashboard">
      <h1>Teacher Dashboard</h1>
      {loading ? (
        <p>Loading...</p>
      ) : (
        <div className="stats-grid">
          <div className="stat-card">
            <h3>My Classes</h3>
            <p className="stat-number">{stats.myClasses}</p>
          </div>
          <div className="stat-card">
            <h3>Total Students</h3>
            <p className="stat-number">{stats.totalStudents}</p>
          </div>
        </div>
      )}
    </div>
  );
}

export default Dashboard;
