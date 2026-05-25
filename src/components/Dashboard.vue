<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue'
import StatCard from './StatCard.vue'
import SignalItem from './SignalItem.vue'
import ToastNotification from './ToastNotification.vue'

const stats = ref([
  { title: 'Pasien Aktif', value: 124, icon: 'fa-solid fa-bed', colorClass: 'icon-blue' },
  { title: 'Sinyal Hari Ini', value: 0, icon: 'fa-solid fa-bell-concierge', colorClass: 'icon-green' },
  { title: 'Panggilan Darurat', value: 0, icon: 'fa-solid fa-triangle-exclamation', colorClass: 'icon-red' },
  { title: 'Kesiapan Sistem', value: '99%', icon: 'fa-solid fa-microchip', colorClass: 'icon-purple' }
])

const signals = ref([])
let interval;

// Notification state
const toasts = ref([])
let lastSignalsCount = -1

// Pagination state
const currentPage = ref(1)
const itemsPerPage = 5

const totalPages = computed(() => Math.ceil(signals.value.length / itemsPerPage))
const paginatedSignals = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage
  return signals.value.slice(start, start + itemsPerPage)
})

const prevPage = () => {
  if (currentPage.value > 1) currentPage.value--
}
const nextPage = () => {
  if (currentPage.value < totalPages.value) currentPage.value++
}

const showToast = (message, type) => {
  const id = Date.now() + Math.random()
  toasts.value.push({ id, message, type })
}

const removeToast = (id) => {
  toasts.value = toasts.value.filter(t => t.id !== id)
}

const fetchSignals = async () => {
  try {
    const res = await fetch('http://localhost:3000/api/signals');
    const data = await res.json();
    
    // Sort descending by date
    data.sort((a, b) => new Date(b.createdAt) - new Date(a.createdAt))

    // Map backend data to UI format
    signals.value = data.map(signal => {
      let icon = 'fa-solid fa-hand';
      if (signal.code.fingerCount === 2) icon = 'fa-solid fa-hand-pointer';
      if (signal.code.fingerCount === 3) icon = 'fa-solid fa-hand-peace';
      
      return {
        id: signal.id,
        icon: icon,
        title: `Ruang ${signal.room.roomNumber} - Kode ${signal.code.fingerCount} (${signal.code.urgencyLevel})`,
        description: `Deteksi ${signal.code.fingerCount} jari. ${signal.code.meaning}.`,
        time: new Date(signal.createdAt).toLocaleTimeString(),
        isUrgent: signal.code.urgencyLevel === 'High',
        status: signal.status
      };
    });
    
    // Check for new signals
    if (lastSignalsCount !== -1 && data.length > lastSignalsCount) {
      const newSignal = signals.value[0]
      showToast(newSignal.title + ' - ' + newSignal.description, newSignal.isUrgent ? 'error' : 'info')
    }
    lastSignalsCount = data.length
    
    // Update stats
    stats.value[1].value = signals.value.length;
    stats.value[2].value = signals.value.filter(s => s.isUrgent).length;
    
  } catch(e) {
    console.error("Gagal mengambil data dari backend", e);
  }
}

onMounted(() => {
  fetchSignals();
  interval = setInterval(fetchSignals, 2000); // Polling setiap 2 detik
})

onUnmounted(() => {
  clearInterval(interval);
})
</script>

<template>
  <div class="container">
    
    <!-- Toast Notifications -->
    <ToastNotification 
      v-for="toast in toasts" 
      :key="toast.id" 
      :message="toast.message" 
      :type="toast.type" 
      :onClose="() => removeToast(toast.id)"
    />

    <div class="page-title">
      <h1>Overview Dashboard</h1>
      <p>Smart Patient Movement Detector Control Center</p>
    </div>

    <!-- Stats -->
    <div class="stats-grid">
      <StatCard 
        v-for="(stat, index) in stats" 
        :key="index"
        :title="stat.title"
        :value="stat.value"
        :icon="stat.icon"
        :colorClass="stat.colorClass"
      />
    </div>

    <!-- Main Sections -->
    <div class="content-grid">
      <!-- Left: Recent Signals -->
      <div class="card">
        <div class="card-header">
          <h2 class="card-title">Sinyal Panggilan Terkini</h2>
          <button class="btn" @click="fetchSignals"><i class="fa-solid fa-rotate-right"></i> Refresh</button>
        </div>
        
        <div class="signal-list">
          <SignalItem
            v-for="signal in paginatedSignals"
            :key="signal.id"
            :icon="signal.icon"
            :title="signal.title"
            :description="signal.description"
            :time="signal.time"
            :isUrgent="signal.isUrgent"
          />
          <div v-if="paginatedSignals.length === 0" style="text-align: center; color: var(--text-muted); padding: 20px;">
            Belum ada sinyal hari ini.
          </div>
        </div>

        <!-- Pagination Controls -->
        <div class="pagination" v-if="totalPages > 1">
          <button class="page-btn" @click="prevPage" :disabled="currentPage === 1"><i class="fa-solid fa-chevron-left"></i> Prev</button>
          <span>Page {{ currentPage }} of {{ totalPages }}</span>
          <button class="page-btn" @click="nextPage" :disabled="currentPage === totalPages">Next <i class="fa-solid fa-chevron-right"></i></button>
        </div>
      </div>

      <!-- Right: System Status -->
      <div class="card">
        <div class="card-header">
          <h2 class="card-title">Status Perangkat IoT</h2>
        </div>
        <div style="text-align: center; padding: 20px 0;">
          <img src="https://cdn-icons-png.flaticon.com/512/3256/3256150.png" alt="Camera" style="width: 100px; opacity: 0.9; margin-bottom: 24px; filter: drop-shadow(0 10px 10px rgba(0,0,0,0.1));">
          <h3 style="font-size: 22px; margin-bottom: 8px; color: var(--text-main); font-weight: 700;">Kamera Aktif</h3>
          <p style="color: var(--text-muted); font-size: 15px; margin-bottom: 28px; line-height: 1.5;">AI MediaPipe Hand Tracker berjalan optimal di Ruang 102.</p>
          
          <div style="display: flex; gap: 12px; justify-content: center;">
            <span style="background: #dcfce7; color: #16a34a; padding: 8px 16px; border-radius: 30px; font-size: 14px; font-weight: 600; display: flex; align-items: center; gap: 8px; box-shadow: 0 4px 6px rgba(22, 163, 74, 0.1);">
              <span style="width: 10px; height: 10px; background: #16a34a; border-radius: 50%; display: inline-block; box-shadow: 0 0 0 3px rgba(22,163,74,0.2);"></span> 
              Online & Monitoring
            </span>
          </div>
        </div>
      </div>
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
}

.page-title {
  margin-bottom: 32px;
}

.page-title h1 {
  font-size: 28px;
  font-weight: 700;
  color: var(--text-main);
  margin-bottom: 8px;
}

.page-title p {
  color: var(--text-muted);
  font-size: 16px;
}

/* Stats Cards */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 24px;
  margin-bottom: 32px;
}

/* Main Section */
.content-grid {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 24px;
}

.card {
  background: var(--card-bg);
  border-radius: 24px;
  padding: 32px;
  border: 1px solid rgba(255,255,255,0.5);
  box-shadow: var(--shadow);
  transition: var(--transition);
}

.card:hover {
  box-shadow: var(--shadow-hover);
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
}

.card-title {
  font-size: 18px;
  font-weight: 700;
  color: var(--text-main);
}

.btn {
  background: linear-gradient(135deg, var(--primary), var(--primary-dark));
  color: white;
  border: none;
  padding: 10px 24px;
  border-radius: 10px;
  font-weight: 600;
  cursor: pointer;
  transition: var(--transition);
  font-family: inherit;
  display: flex;
  align-items: center;
  gap: 8px;
  box-shadow: 0 4px 10px rgba(14, 165, 233, 0.2);
}

.btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 15px rgba(14, 165, 233, 0.3);
}

/* Active Signals List */
.signal-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

/* Pagination */
.pagination {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 24px;
  padding-top: 20px;
  border-top: 1px solid var(--border);
  color: var(--text-muted);
  font-size: 14px;
}

.page-btn {
  background: white;
  border: 1px solid var(--border);
  padding: 8px 16px;
  border-radius: 8px;
  cursor: pointer;
  font-family: inherit;
  color: var(--text-main);
  transition: 0.2s;
  display: flex;
  align-items: center;
  gap: 8px;
}

.page-btn:hover:not(:disabled) {
  border-color: var(--primary);
  color: var(--primary);
}

.page-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  background: var(--bg-main);
}

@media (max-width: 992px) {
  .content-grid {
    grid-template-columns: 1fr;
  }
}
</style>
