<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const props = defineProps({
  message: {
    type: String,
    required: true
  },
  type: {
    type: String,
    default: 'info' // 'info' or 'error' (urgent)
  },
  duration: {
    type: Number,
    default: 5000
  },
  onClose: {
    type: Function,
    required: true
  }
})

const isVisible = ref(true)
let timeoutId;

onMounted(() => {
  // Play sound
  const audioContext = new (window.AudioContext || window.webkitAudioContext)()
  const oscillator = audioContext.createOscillator()
  const gainNode = audioContext.createGain()
  
  oscillator.connect(gainNode)
  gainNode.connect(audioContext.destination)
  
  if (props.type === 'error') {
    oscillator.type = 'square'
    oscillator.frequency.setValueAtTime(880, audioContext.currentTime) // A5
    oscillator.frequency.setValueAtTime(1108.73, audioContext.currentTime + 0.2) // C#6
    gainNode.gain.setValueAtTime(0.1, audioContext.currentTime)
  } else {
    oscillator.type = 'sine'
    oscillator.frequency.setValueAtTime(523.25, audioContext.currentTime) // C5
    oscillator.frequency.setValueAtTime(659.25, audioContext.currentTime + 0.1) // E5
    gainNode.gain.setValueAtTime(0.1, audioContext.currentTime)
  }
  
  oscillator.start()
  oscillator.stop(audioContext.currentTime + 0.4)

  // Auto hide
  timeoutId = setTimeout(() => {
    close()
  }, props.duration)
})

onUnmounted(() => {
  clearTimeout(timeoutId)
})

const close = () => {
  isVisible.value = false
  setTimeout(props.onClose, 300) // wait for animation
}
</script>

<template>
  <div v-if="isVisible" :class="['toast-notification', type]">
    <div class="toast-icon">
      <i v-if="type === 'error'" class="fa-solid fa-triangle-exclamation"></i>
      <i v-else class="fa-solid fa-bell"></i>
    </div>
    <div class="toast-content">
      <h4>{{ type === 'error' ? 'Panggilan Darurat!' : 'Sinyal Baru Masuk' }}</h4>
      <p>{{ message }}</p>
    </div>
    <button class="close-btn" @click="close">
      <i class="fa-solid fa-xmark"></i>
    </button>
  </div>
</template>

<style scoped>
.toast-notification {
  position: fixed;
  top: 24px;
  right: 24px;
  background: white;
  border-radius: 16px;
  padding: 16px 20px;
  display: flex;
  align-items: flex-start;
  gap: 16px;
  box-shadow: 0 10px 40px rgba(0,0,0,0.15);
  z-index: 9999;
  animation: slideIn 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
  max-width: 350px;
  border-left: 6px solid var(--primary);
}

.toast-notification.error {
  border-left-color: #ef4444;
}

.toast-icon {
  width: 40px;
  height: 40px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  flex-shrink: 0;
}

.toast-notification.info .toast-icon {
  background: #e0f2fe;
  color: var(--primary);
}

.toast-notification.error .toast-icon {
  background: #fee2e2;
  color: #ef4444;
  animation: pulse 1s infinite;
}

.toast-content h4 {
  margin: 0 0 4px 0;
  font-size: 16px;
  color: var(--text-main);
}

.toast-content p {
  margin: 0;
  font-size: 14px;
  color: var(--text-muted);
  line-height: 1.4;
}

.close-btn {
  background: none;
  border: none;
  color: #94a3b8;
  cursor: pointer;
  padding: 4px;
  margin-left: auto;
  font-size: 16px;
  transition: 0.2s;
}

.close-btn:hover {
  color: var(--text-main);
}

@keyframes slideIn {
  from {
    transform: translateX(100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

@keyframes pulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.1); }
  100% { transform: scale(1); }
}
</style>
