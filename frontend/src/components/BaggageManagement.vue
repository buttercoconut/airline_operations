<template>
  <div class="baggage-management">
    <h2>수하물 관리</h2>
    <form @submit.prevent="addBaggage">
      <div class="form-group">
        <label for="passengerId">여객 ID</label>
        <input type="text" id="passengerId" v-model="baggage.passenger_id" required />
      </div>
      <div class="form-group">
        <label for="weight">무게 (kg)</label>
        <input type="number" id="weight" v-model="baggage.weight" required />
      </div>
      <button type="submit">추가</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { addBaggage } from '@/services/api';

const baggage = ref({
  passenger_id: '',
  weight: null
});

const addBaggage = async () => {
  try {
    await addBaggage(baggage.value);
    alert('수하물 등록 완료');
  } catch (e) {
    alert('등록 실패: ' + e.message);
  }
};
</script>

<style scoped>
.baggage-management {
  max-width: 400px;
  margin: auto;
}
.form-group {
  margin-bottom: 1rem;
}
</style>