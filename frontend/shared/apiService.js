import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api/v1';

const api = axios.create({
  baseURL: API_BASE_URL,
});

// Add token to headers if available
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('accessToken');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export const authService = {
  register: (email, password, fullName, role) =>
    api.post('/users/register', { email, password, full_name: fullName, role }),
  login: (email, password) =>
    api.post('/users/login', { email, password }),
};

export const studentService = {
  getStudents: (skip = 0, limit = 100) =>
    api.get('/students', { params: { skip, limit } }),
  getStudent: (id) =>
    api.get(`/students/${id}`),
  createStudent: (data) =>
    api.post('/students', data),
};

export const teacherService = {
  getTeachers: (skip = 0, limit = 100) =>
    api.get('/teachers', { params: { skip, limit } }),
  getTeacher: (id) =>
    api.get(`/teachers/${id}`),
  createTeacher: (data) =>
    api.post('/teachers', data),
};

export const classroomService = {
  getClassrooms: (skip = 0, limit = 100) =>
    api.get('/classrooms', { params: { skip, limit } }),
  getClassroom: (id) =>
    api.get(`/classrooms/${id}`),
  createClassroom: (data) =>
    api.post('/classrooms', data),
};

export const attendanceService = {
  getAttendance: (skip = 0, limit = 100) =>
    api.get('/attendance', { params: { skip, limit } }),
  createAttendance: (data) =>
    api.post('/attendance', data),
};

export const feeService = {
  getFeePlans: (skip = 0, limit = 100) =>
    api.get('/fees/plans', { params: { skip, limit } }),
  createFeePlan: (data) =>
    api.post('/fees/plans', data),
  getFeePayments: (skip = 0, limit = 100) =>
    api.get('/fees/payments', { params: { skip, limit } }),
  createFeePayment: (data) =>
    api.post('/fees/payments', data),
};

export const timetableService = {
  getTimetable: (skip = 0, limit = 100) =>
    api.get('/timetable', { params: { skip, limit } }),
  createTimetableSlot: (data) =>
    api.post('/timetable', data),
};

export const notificationService = {
  getNotifications: (skip = 0, limit = 100) =>
    api.get('/notifications', { params: { skip, limit } }),
  createNotification: (data) =>
    api.post('/notifications', data),
};

export default api;
