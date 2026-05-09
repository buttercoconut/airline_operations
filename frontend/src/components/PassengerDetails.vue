<template>
  <div class="passenger-details">
    <h2>여객 상세 정보</h2>
    <form @submit.prevent="submitDetails">
      <div class="form-group">
        <label for="name">이름</label>
        <input type="text" id="name" v-model="details.name" required />
      </div>
      <div class="form-group">
        <label for="passport">여권 번호</label>
        <input type="text" id="passport" v-model="details.passport" required />
      </div>
      <div class="form-group">
        <label for="age">나이</label>
        <input type="number" id="age" v-model="details.age" required />
      </div>
      <button type="submit">저장</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { updatePassengerDetails } from '@/services/api';

const details = ref({
  name: '',
  passport: '',
  age: null
});

const submitDetails = async () => {
  try {
    const res = await updatePassengerDetails(details.value);
    alert('여객 정보 저장 완료');
  } catch (e) {
    alert('저장 실패: ' + e.message);
  }
};
</script>

<style scoped>
.passenger-details {
  max-width: 400px;
  margin: auto;
}
.form-group {
  margin-bottom: 1rem;
}
</style>