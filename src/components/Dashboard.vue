<script setup>
import StatCard from './StatCard.vue'
import SignalItem from './SignalItem.vue'

const stats = [
  { title: 'Pasien Aktif', value: 124, icon: 'fa-solid fa-bed', colorClass: 'icon-blue' },
  { title: 'Sinyal Hari Ini', value: 38, icon: 'fa-solid fa-bell-concierge', colorClass: 'icon-green' },
  { title: 'Panggilan Darurat', value: 2, icon: 'fa-solid fa-triangle-exclamation', colorClass: 'icon-red' },
  { title: 'Kesiapan Sistem', value: '99%', icon: 'fa-solid fa-microchip', colorClass: 'icon-purple' }
]

const signals = [
  {
    icon: 'fa-solid fa-hand',
    title: 'Ruang 102 - Kode 4 (Darurat)',
    description: 'Deteksi 5 jari. Bantuan dokter segera dibutuhkan.',
    time: 'Baru saja',
    isUrgent: true
  },
  {
    icon: 'fa-solid fa-hand-pointer',
    title: 'Ruang 205 - Kode 1 (Biasa)',
    description: 'Deteksi 2 jari. Pasien meminta bantuan minum/makan.',
    time: '10 min lalu',
    isUrgent: false
  },
  {
    icon: 'fa-solid fa-hand-peace',
    title: 'Ruang 102 - Kode 2 (Menengah)',
    description: 'Deteksi 3 jari. Pasien membutuhkan bantuan ke toilet.',
    time: '45 min lalu',
    isUrgent: false
  }
]
</script>

<template>
  <div class="container">
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
          <button class="btn"><i class="fa-solid fa-rotate-right"></i> Refresh</button>
        </div>
        
        <div class="signal-list">
          <SignalItem
            v-for="(signal, index) in signals"
            :key="index"
            :icon="signal.icon"
            :title="signal.title"
            :description="signal.description"
            :time="signal.time"
            :isUrgent="signal.isUrgent"
          />
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

@media (max-width: 992px) {
  .content-grid {
    grid-template-columns: 1fr;
  }
}
</style>
