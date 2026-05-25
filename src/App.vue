<script setup>
import { ref } from 'vue'
import Sidebar from './components/Sidebar.vue'
import TopBar from './components/TopBar.vue'

const isSidebarOpen = ref(false)

const toggleSidebar = () => {
  isSidebarOpen.value = !isSidebarOpen.value
}
</script>

<template>
  <Sidebar :isOpen="isSidebarOpen" />
  
  <main id="main-content">
    <TopBar @toggle-sidebar="toggleSidebar" />
    <router-view />
    
    <footer>
      &copy; 2026 SMADER (Smart Patient Movement Detector). Dipersembahkan oleh <a href="#">UROTERA TEAM</a> - Institut Teknologi Sumatera.
    </footer>
  </main>
</template>

<style scoped>
#main-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  min-width: 0;
}

footer {
  text-align: center;
  padding: 24px;
  color: var(--text-muted);
  font-size: 14px;
  border-top: 1px solid var(--border);
  margin-top: auto;
}

footer a {
  color: var(--primary);
  text-decoration: none;
  font-weight: 600;
}
</style>
