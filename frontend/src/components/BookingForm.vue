<template>
  <div class="booking-form">
    <h2>항공권 예약</h2>
    <form @submit.prevent="submit">
      <label>항공편 ID:</label>
      <input type="text" v-model="flightId" required />
      <label>이름:</label>
      <input type="text" v-model="name" required />
      <button type="submit">예약하기</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const flightId = ref('')
const name = ref('')
const router = useRouter()

function submit() {
  // 간단히 예약 정보를 로컬스토리지에 저장
  const booking = { flightId: flightId.value, name: name.value }
  localStorage.setItem('booking', JSON.stringify(booking))
  router.push('/passenger')
}
</script>

<style scoped>
.booking-form { padding: 10px; }
label { display: block; margin-top: 10px; }
button { margin-top: 10px; }
</style>
