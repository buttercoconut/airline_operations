<template>
  <div class="booking-form">
    <h2>예약 폼</h2>
    <form @submit.prevent="submitBooking">
      <div class="form-group">
        <label for="flightId">항공편 ID</label>
        <input type="text" id="flightId" v-model="booking.flight_id" required />
      </div>
      <div class="form-group">
        <label for="seatNumber">좌석 번호</label>
        <input type="text" id="seatNumber" v-model="booking.seat_number" required />
      </div>
      <div class="form-group">
        <label for="passengerName">여객 이름</label>
        <input type="text" id="passengerName" v-model="booking.passenger_name" required />
      </div>
      <button type="submit">예약하기</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { createBooking } from '@/services/api';

const booking = ref({
  flight_id: '',
  seat_number: '',
  passenger_name: ''
});

const submitBooking = async () => {
  try {
    const response = await createBooking(booking.value);
    alert(`예약 성공: ${response.data.booking_id}`);
  } catch (err) {
    alert(`예약 실패: ${err.message}`);
  }
};
</script>

<style scoped>
.booking-form {
  max-width: 400px;
  margin: auto;
}
.form-group {
  margin-bottom: 1rem;
}
</style>