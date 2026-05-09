<template>
  <div class="passenger-details">
    <h2>여행자 정보 입력</h2>
    <form @submit.prevent="submit">
      <label>이름:</label>
      <input type="text" v-model="name" required />
      <label>연락처:</label>
      <input type="tel" v-model="phone" required />
      <button type="submit">완료</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const name = ref('')
const phone = ref('')

function submit() {
  const passenger = { name: name.value, phone: phone.value }
  localStorage.setItem('passenger', JSON.stringify(passenger))
  alert('예약이 완료되었습니다!')
}
</script>

<style scoped>
.passenger-details { padding: 10px; }
label { display: block; margin-top: 10px; }
button { margin-top: 10px; }
</style>
