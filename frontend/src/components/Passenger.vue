<template>
  <div class="passenger-details">
    <h2>여행자 정보 입력</h2>
    <form @submit.prevent="handleSubmit">
      <label>이름:<input v-model="name" required />
      <label>연락처:<input type="tel" v-model="contact" required />
      <label>이메일:<input type="email" v-model="email" required />
      <button type="submit">완료</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { submitPassenger } from '../services/api'

const name = ref('')
const contact = ref('')
const email = ref('')

async function handleSubmit() {
  try {
    await submitPassenger({ name: name.value, contact: contact.value, email: email.value })
    alert('예약이 완료되었습니다!')
  } catch (e) {
    console.error(e)
  }
}
</script>

<style scoped>
.passenger-details { padding: 10px; }
</style>
