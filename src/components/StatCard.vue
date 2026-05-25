<script setup>
defineProps({
  title: String,
  value: [String, Number],
  icon: String,
  colorClass: String
})
</script>

<template>
  <div class="stat-card">
    <div class="stat-info">
      <h3>{{ title }}</h3>
      <div class="value">{{ value }}</div>
    </div>
    <div class="stat-icon" :class="colorClass">
      <i :class="icon"></i>
    </div>
  </div>
</template>

<style scoped>
.stat-card {
  background: var(--card-bg);
  backdrop-filter: blur(10px);
  border-radius: 20px;
  padding: 24px;
  border: 1px solid rgba(255,255,255,0.5);
  box-shadow: var(--shadow);
  transition: var(--transition);
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  position: relative;
  overflow: hidden;
}

.stat-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 4px;
  background: linear-gradient(90deg, var(--primary), transparent);
  opacity: 0;
  transition: var(--transition);
}

.stat-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-hover);
}

.stat-card:hover::before {
  opacity: 1;
}

.stat-info h3 {
  font-size: 13px;
  color: var(--text-muted);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 8px;
}

.stat-info .value {
  font-size: 36px;
  font-weight: 700;
  color: var(--text-main);
}

.stat-icon {
  width: 52px;
  height: 52px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
}

.icon-blue { background: #e0f2fe; color: #0284c7; }
.icon-green { background: #dcfce7; color: #16a34a; }
.icon-red { background: #fee2e2; color: #dc2626; }
.icon-purple { background: #f3e8ff; color: #9333ea; }
</style>
