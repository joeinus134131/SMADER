<script setup>
import { useRoute } from 'vue-router'
import { computed } from 'vue'

const route = useRoute()
const pageName = computed(() => route.name)
</script>

<template>
  <div class="container">
    <div class="card placeholder-card">
      <div class="icon-wrapper">
        <i class="fa-solid fa-person-digging"></i>
      </div>
      <h2>Halaman {{ pageName }}</h2>
      <p>Modul ini sedang dalam tahap pengembangan (Coming Soon).</p>
      <router-link to="/" class="btn">Kembali ke Dashboard</router-link>
    </div>
  </div>
</template>

<style scoped>
.container {
  padding: 32px;
  flex: 1;
  max-width: 1400px;
  margin: 0 auto;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.placeholder-card {
  text-align: center;
  padding: 60px 40px;
  max-width: 500px;
  width: 100%;
}

.icon-wrapper i {
  font-size: 64px;
  color: var(--primary);
  margin-bottom: 24px;
  opacity: 0.8;
}

h2 {
  font-size: 24px;
  color: var(--text-main);
  margin-bottom: 12px;
}

p {
  color: var(--text-muted);
  margin-bottom: 32px;
  line-height: 1.6;
}

.btn {
  display: inline-block;
  background: linear-gradient(135deg, var(--primary), var(--primary-dark));
  color: white;
  padding: 12px 24px;
  border-radius: 12px;
  text-decoration: none;
  font-weight: 600;
  transition: var(--transition);
}

.btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 15px rgba(14, 165, 233, 0.3);
}
</style>
