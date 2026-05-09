
import { createRouter, createWebHistory } from 'vue-router';
import BookingForm from '@/components/BookingForm.vue';
import PassengerDetails from '@/components/PassengerDetails.vue';
import BaggageManagement from '@/components/BaggageManagement.vue';
import MaintenanceDashboard from '@/components/MaintenanceDashboard.vue';

const routes = [
  { path: '/', component: BookingForm, name: 'Booking' },
  { path: '/passenger', component: PassengerDetails, name: 'Passenger' },
  { path: '/baggage', component: BaggageManagement, name: 'Baggage' },
  { path: '/maintenance', component: MaintenanceDashboard, name: 'Maintenance' },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
