<template>
  <div class="flight-schedule">
    <h2>Flight Schedule</h2>
    <table>
      <thead>
        <tr>
          <th>Flight No.</th>
          <th>Origin</th>
          <th>Destination</th>
          <th>Departure</th>
          <th>Arrival</th>
          <th>Seats Available</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="flight in flights" :key="flight.id">
          <td>{{ flight.flight_number }}</td>
          <td>{{ flight.origin }}</td>
          <td>{{ flight.destination }}</td>
          <td>{{ formatDate(flight.departure_time) }}</td>
          <td>{{ formatDate(flight.arrival_time) }}</td>
          <td>{{ flight.seats_available }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const flights = ref([])

const fetchFlights = async () => {
  try {
    const response = await axios.get('http://localhost:8000/api/flight/')
    flights.value = response.data
  } catch (err) {
    console.error('Error fetching flights', err)
  }
}

const formatDate = (iso) => {
  const d = new Date(iso)
  return d.toLocaleString()
}

onMounted(() => {
  fetchFlights()
})
</script>

<style scoped>
.flight-schedule {
  margin-top: 20px;
}
.flight-schedule table {
  width: 100%;
  border-collapse: collapse;
}
.flight-schedule th, .flight-schedule td {
  border: 1px solid #ddd;
  padding: 8px;
}
.flight-schedule th {
  background-color: #f2f2f2;
}
</style>