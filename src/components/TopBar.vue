<script setup>
defineEmits(['toggle-sidebar'])
</script>

<template>
  <header class="topbar">
    <button class="toggle-btn" @click="$emit('toggle-sidebar')">
      <i class="fa-solid fa-bars"></i>
    </button>
    <div style="flex: 1;"></div> <!-- Spacer -->
    <div class="user-profile">
      <span>Nurse Station Alpha</span>
      <img src="https://ui-avatars.com/api/?name=Nurse+Station&background=0ea5e9&color=fff&rounded=true" alt="Profile">
    </div>
  </header>
</template>

<style scoped>
.topbar {
  height: 72px;
  background-color: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 32px;
  position: sticky;
  top: 0;
  z-index: 50;
}

.toggle-btn {
  background: none;
  border: none;
  font-size: 24px;
  color: var(--text-muted);
  cursor: pointer;
  transition: var(--transition);
  display: none; /* Only show on mobile */
}

.toggle-btn:hover {
  color: var(--primary);
}

.user-profile {
  display: flex;
  align-items: center;
  gap: 12px;
  cursor: pointer;
  padding: 6px 12px;
  border-radius: 30px;
  transition: var(--transition);
}

.user-profile:hover {
  background: var(--secondary);
}

.user-profile img {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid var(--primary);
}

.user-profile span {
  font-weight: 600;
  color: var(--text-main);
  font-size: 14px;
}

@media (max-width: 768px) {
  .toggle-btn {
    display: block;
  }
}
</style>
