# SMADER - Smart Patient Movement Detector

SMADER adalah piranti cerdas yang dibuat untuk mengefisienkan pekerjaan perawat dalam melayani kebutuhan pasien. Aplikasi ini menggunakan Computer Vision (MediaPipe) untuk mendeteksi gestur tangan pasien sebagai sinyal panggilan bantuan ke *nurse station* atau sistem *dashboard*.

## 🛠️ Fitur Utama
- **Deteksi AI Responsif**: Menggunakan Google MediaPipe untuk melacak gestur jari pasien dengan akurasi tinggi dan tahan terhadap gangguan pencahayaan.
- **Smart Notification**: Otomatis mengirim HTTP Request ke server dashboard berdasarkan jumlah jari yang diangkat.
- **Web Dashboard**: Antarmuka berbasis web untuk memonitor data panggilan darurat, data pasien, dan tenaga medis.

## 📦 Instalasi & Cara Penggunaan

1. **Clone repositori ini atau buka di direktori Anda.**
2. **Install semua dependensi Python:**
   Pastikan Anda menggunakan Python 3.8 ke atas.
   ```bash
   pip install -r requirements.txt
   ```
3. **Konfigurasi Server:**
   Buka file `final.py` dan sesuaikan variabel konfigurasi di bagian atas:
   - `URL_SERVER`: Endpoint tujuan API.
   - `NOMOR_RUANG`: Nomor ruang instalasi alat (contoh: 102).
   - `COOLDOWN_SECONDS`: Jeda waktu antarpanggilan (agar tidak *spam* server).
4. **Jalankan Aplikasi Deteksi:**
   Pastikan webcam sudah tersambung, lalu jalankan:
   ```bash
   python final.py
   ```
5. **Akses Dashboard Web:**
   Buka file `index.html` pada browser Anda.

## 🤝 Kontribusi
Dipersembahkan oleh tim UROTERA Institut Teknologi Sumatera.
