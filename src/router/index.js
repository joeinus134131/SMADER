import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '../components/Dashboard.vue'
import Placeholder from '../views/Placeholder.vue'

const routes = [
  {
    path: '/',
    name: 'Dashboard',
    component: Dashboard
  },
  {
    path: '/data-pasien',
    name: 'Data Pasien',
    component: Placeholder
  },
  {
    path: '/data-kode',
    name: 'Data Kode',
    component: Placeholder
  },
  {
    path: '/data-dokter',
    name: 'Data Dokter',
    component: Placeholder
  },
  {
    path: '/data-perawat',
    name: 'Data Perawat',
    component: Placeholder
  },
  {
    path: '/bantuan',
    name: 'Bantuan',
    component: Placeholder
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
