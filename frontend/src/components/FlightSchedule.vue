<template>
  <div class="flight-schedule">
    <h2>항공편 일정</h2>
    <ul>
      <li v-for="flight in flights" :key="flight.id">
        {{ flight.flightNumber }} - {{ flight.origin }} → {{ flight.destination }}
        <router-link :to="{ path: '/booking', query: { flightId: flight.id } }">예약하기</router-link>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { fetchFlightSchedule } from '../services/api'

const flights = ref([])

onMounted(async () => {
  try {
    flights.value = await fetchFlightSchedule()
  } catch (e) {
    console.error(e)
  }
})
</script>

<style scoped>
.flight-schedule { padding: 10px; }
</style>
