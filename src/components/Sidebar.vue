<script setup>
defineProps({
  isOpen: {
    type: Boolean,
    default: false
  }
})
</script>

<template>
  <aside id="sidebar" :class="{ 'open': isOpen }">
    <div class="sidebar-header">
      <i class="fa-solid fa-hand-holding-medical"></i>
      <h2>SMADER</h2>
    </div>
    <ul class="sidebar-menu">
      <li><a href="#" class="menu-item active"><i class="fa-solid fa-chart-pie"></i> Dashboard</a></li>
      <li><a href="#" class="menu-item"><i class="fa-solid fa-bed-pulse"></i> Data Pasien</a></li>
      <li><a href="#" class="menu-item"><i class="fa-solid fa-list-check"></i> Data Kode</a></li>
      <li><a href="#" class="menu-item"><i class="fa-solid fa-user-doctor"></i> Data Dokter</a></li>
      <li><a href="#" class="menu-item"><i class="fa-solid fa-user-nurse"></i> Data Perawat</a></li>
      <li style="margin-top: 40px;"><a href="#" class="menu-item"><i class="fa-solid fa-circle-info"></i> Bantuan</a></li>
    </ul>
  </aside>
</template>

<style scoped>
#sidebar {
  width: 260px;
  background-color: var(--sidebar);
  border-right: 1px solid var(--border);
  display: flex;
  flex-direction: column;
  transition: var(--transition);
  z-index: 100;
  box-shadow: 4px 0 10px rgba(0,0,0,0.01);
}

.sidebar-header {
  padding: 24px;
  display: flex;
  align-items: center;
  gap: 12px;
  border-bottom: 1px solid var(--border);
}

.sidebar-header i {
  font-size: 24px;
  color: white;
  background: linear-gradient(135deg, var(--primary), var(--primary-dark));
  padding: 10px;
  border-radius: 12px;
  box-shadow: 0 4px 10px rgba(14, 165, 233, 0.3);
}

.sidebar-header h2 {
  font-size: 22px;
  font-weight: 700;
  letter-spacing: 0.5px;
  color: var(--text-main);
}

.sidebar-menu {
  flex: 1;
  padding: 24px 0;
  list-style: none;
}

.menu-item {
  padding: 14px 24px;
  display: flex;
  align-items: center;
  gap: 16px;
  color: var(--text-muted);
  text-decoration: none;
  font-weight: 500;
  transition: var(--transition);
  border-left: 4px solid transparent;
}

.menu-item:hover, .menu-item.active {
  background-color: var(--secondary);
  color: var(--primary-dark);
  border-left-color: var(--primary);
}

.menu-item i {
  font-size: 18px;
  width: 24px;
  text-align: center;
}

@media (max-width: 768px) {
  #sidebar {
    position: fixed;
    transform: translateX(-100%);
    height: 100vh;
  }

  #sidebar.open {
    transform: translateX(0);
  }
}
</style>
