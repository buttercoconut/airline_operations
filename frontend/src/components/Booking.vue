<template>
  <div class="booking-form">
    <h2>항공권 예약</h2>
    <form @submit.prevent="handleSubmit">
      <label>항공편 ID:<input v-model="flightId" readonly />
      <label>이름:<input v-model="name" required />
      <label>좌석 수:<input type="number" v-model.number="seats" min="1" required />
      <button type="submit">예약하기</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { submitBooking } from '../services/api'

const route = useRoute()
const router = useRouter()
const flightId = ref(route.query.flightId || '')
const name = ref('')
const seats = ref(1)

async function handleSubmit() {
  try {
    await submitBooking({ flightId: flightId.value, name: name.value, seats: seats.value })
    router.push('/passenger')
  } catch (e) {
    console.error(e)
  }
}
</script>

<style scoped>
.booking-form { padding: 10px; }
</style>
