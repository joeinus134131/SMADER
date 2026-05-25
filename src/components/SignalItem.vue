<script setup>
defineProps({
  icon: String,
  title: String,
  description: String,
  time: String,
  isUrgent: {
    type: Boolean,
    default: false
  }
})
</script>

<template>
  <div class="signal-item" :class="{ 'urgent': isUrgent }">
    <div class="signal-icon">
      <i :class="icon"></i>
    </div>
    <div class="signal-details">
      <h4>{{ title }}</h4>
      <p>{{ description }}</p>
    </div>
    <div class="signal-time">{{ time }}</div>
  </div>
</template>

<style scoped>
.signal-item {
  display: flex;
  align-items: center;
  gap: 20px;
  padding: 20px;
  background: white;
  border-radius: 16px;
  transition: var(--transition);
  border: 1px solid var(--border);
  border-left: 5px solid var(--primary);
}

.signal-item:hover {
  transform: translateX(5px);
  box-shadow: var(--shadow);
}

.signal-item.urgent {
  border-left-color: #ef4444;
  background: #fffafa;
  border: 1px solid #fee2e2;
  border-left: 5px solid #ef4444;
}

.signal-item.urgent:hover {
  box-shadow: 0 4px 12px rgba(239, 68, 68, 0.1);
}

.signal-icon {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background: var(--secondary);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  color: var(--primary);
}

.signal-item.urgent .signal-icon {
  background: #fee2e2;
  color: #ef4444;
}

.signal-details {
  flex: 1;
}

.signal-details h4 {
  font-size: 16px;
  font-weight: 700;
  margin-bottom: 4px;
  color: var(--text-main);
}

.signal-details p {
  font-size: 14px;
  color: var(--text-muted);
}

.signal-time {
  font-size: 13px;
  font-weight: 600;
  color: var(--text-muted);
  background: var(--background);
  padding: 6px 12px;
  border-radius: 20px;
}
</style>
