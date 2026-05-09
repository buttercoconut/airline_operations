<template>
  <div class="maintenance-dashboard">
    <h2>정비 대시보드</h2>
    <ul>
      <li v-for="(task, index) in tasks" :key="index">
        {{ task.description }} - {{ task.status }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { fetchMaintenanceTasks } from '@/services/api';

const tasks = ref([]);

onMounted(async () => {
  try {
    const res = await fetchMaintenanceTasks();
    tasks.value = res.data.tasks;
  } catch (e) {
    console.error('정비 데이터 로드 실패', e);
  }
});
</script>

<style scoped>
.maintenance-dashboard {
  max-width: 600px;
  margin: auto;
}
ul {
  list-style: none;
  padding: 0;
}
li {
  padding: 0.5rem 0;
  border-bottom: 1px solid #ccc;
}
</style>