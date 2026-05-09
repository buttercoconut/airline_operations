<template>
  <div class="flight-list">
    <h2>Available Flights</h2>
    <ul>
      <li v-for="flight in flights" :key="flight.id">
        {{ flight.flight_number }}: {{ flight.origin }} → {{ flight.destination }}
        <button @click="bookFlight(flight.id)">Book Seat</button>
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import axios from 'axios';

interface Flight {
  id: number;
  flight_number: string;
  origin: string;
  destination: string;
}

const flights = ref<Flight[]>([]);

const fetchFlights = async () => {
  const res = await axios.get('/flights');
  flights.value = res.data;
};

const bookFlight = async (id: number) => {
  try {
    await axios.post(`/flights/${id}/book`);
    alert('Seat booked!');
  } catch (e) {
    alert('Booking failed');
  }
};

onMounted(fetchFlights);
</script>

<style scoped>
.flight-list {
  padding: 1rem;
}
</style>
