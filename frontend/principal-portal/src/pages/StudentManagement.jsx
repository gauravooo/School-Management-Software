import React, { useEffect, useState } from 'react';
import { studentService } from '../../shared/apiService';
import './StudentManagement.css';

function StudentManagement() {
  const [students, setStudents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [newStudent, setNewStudent] = useState({
    first_name: '',
    last_name: '',
    roll_number: '',
    class_id: 1,
  });

  useEffect(() => {
    fetchStudents();
  }, []);

  const fetchStudents = async () => {
    try {
      const response = await studentService.getStudents();
      setStudents(response.data);
    } catch (err) {
      setError('Failed to load students');
    } finally {
      setLoading(false);
    }
  };

  const handleAddStudent = async (e) => {
    e.preventDefault();
    try {
      await studentService.createStudent(newStudent);
      fetchStudents();
      setNewStudent({ first_name: '', last_name: '', roll_number: '', class_id: 1 });
    } catch (err) {
      setError('Failed to add student');
    }
  };

  return (
    <div className="student-management">
      <h2>Student Management</h2>
      
      <div className="add-student-form">
        <h3>Add New Student</h3>
        <form onSubmit={handleAddStudent}>
          <input
            type="text"
            placeholder="First Name"
            value={newStudent.first_name}
            onChange={(e) => setNewStudent({ ...newStudent, first_name: e.target.value })}
            required
          />
          <input
            type="text"
            placeholder="Last Name"
            value={newStudent.last_name}
            onChange={(e) => setNewStudent({ ...newStudent, last_name: e.target.value })}
            required
          />
          <input
            type="text"
            placeholder="Roll Number"
            value={newStudent.roll_number}
            onChange={(e) => setNewStudent({ ...newStudent, roll_number: e.target.value })}
            required
          />
          <button type="submit">Add Student</button>
        </form>
      </div>

      {error && <div className="error-message">{error}</div>}

      {loading ? (
        <p>Loading students...</p>
      ) : (
        <div className="students-table">
          <table>
            <thead>
              <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Roll Number</th>
                <th>Class ID</th>
              </tr>
            </thead>
            <tbody>
              {students.length > 0 ? (
                students.map((student) => (
                  <tr key={student.id}>
                    <td>{student.id}</td>
                    <td>{student.first_name} {student.last_name}</td>
                    <td>{student.roll_number}</td>
                    <td>{student.class_id}</td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan="4">No students found</td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default StudentManagement;
