<!--
  API 서비스 모듈
  axios 인스턴스를 사용해 백엔드와 통신합니다.
-->

import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api', // 실제 백엔드 URL로 교체
  timeout: 10000,
});

export const createBooking = (data) => api.post('/bookings', data);
export const updatePassengerDetails = (data) => api.put('/passengers', data);
export const addBaggage = (data) => api.post('/baggage', data);
export const fetchMaintenanceTasks = () => api.get('/maintenance/tasks');
