import { createRouter, createWebHistory } from 'vue-router'
import FlightSchedule from '../components/FlightSchedule.vue'
import Booking from '../components/Booking.vue'
import Passenger from '../components/Passenger.vue'

const routes = [
  { path: '/', component: FlightSchedule },
  { path: '/booking', component: Booking },
  { path: '/passenger', component: Passenger }
]

export default createRouter({
  history: createWebHistory(),
  routes
})
