# SMADER - Smart Patient Movement Detector

SMADER adalah piranti cerdas yang dibuat untuk mengefisienkan pekerjaan perawat dalam melayani kebutuhan pasien. Aplikasi ini menggunakan Computer Vision (MediaPipe) untuk mendeteksi gestur tangan pasien sebagai sinyal panggilan bantuan ke *nurse station* atau sistem *dashboard*.

## 🛠️ Fitur Utama
- **Deteksi AI Responsif**: Menggunakan Google MediaPipe (Tasks API) untuk melacak gestur jari pasien dengan akurasi tinggi dan tahan terhadap gangguan pencahayaan. Model AI (`hand_landmarker.task`) akan diunduh secara otomatis pada saat pertama kali aplikasi dijalankan.
- **Smart Notification**: Otomatis mengirim HTTP Request ke server dashboard berdasarkan jumlah jari yang diangkat.
- **Web Dashboard**: Antarmuka berbasis web premium (Vanilla CSS/Glassmorphism) untuk memonitor data panggilan darurat, data pasien, dan tenaga medis.

## 📦 Instalasi & Cara Penggunaan

Penggunaan **Conda** dengan **Python 3.11** sangat disarankan untuk menghindari masalah inkompatibilitas library MediaPipe di macOS versi terbaru (terutama Mac dengan chip Apple Silicon M1/M2/M3).

### Langkah 1: Persiapan Environment (Conda)
1. Buka terminal Anda.
2. Buat *virtual environment* baru bernama `smader_env` dengan Python 3.11:
   ```bash
   conda create -n smader_env python=3.11 -y
   ```
3. Aktifkan *environment* tersebut:
   ```bash
   conda activate smader_env
   ```

### Langkah 2: Instalasi Library
Pastikan Anda berada di dalam folder project ini, lalu jalankan:
```bash
pip install -r requirements.txt
```

### Langkah 3: Konfigurasi Server
Buka file `final.py` dan sesuaikan variabel konfigurasi di bagian atas:
- `URL_SERVER`: Endpoint tujuan API.
- `NOMOR_RUANG`: Nomor ruang instalasi alat (contoh: 102).
- `COOLDOWN_SECONDS`: Jeda waktu antarpanggilan (standar 3 detik agar tidak *spam* server).

### Langkah 4: Menjalankan Aplikasi AI
Pastikan webcam (kamera) Anda sudah tersambung dan tidak digunakan oleh aplikasi lain, lalu jalankan:
```bash
python final.py
```
> **Catatan Penting**: Gunakan perintah `python` (bukan `python3`) agar script dieksekusi oleh Python milik Conda. Pada saat dijalankan pertama kali, script akan mengunduh model AI dari server Google (ukuran hanya beberapa MB).

### Langkah 5: Membuka Dashboard Web
Buka file `index.html` pada browser Anda (Klik kanan file -> Open With -> Google Chrome/Safari) untuk memantau status notifikasi dan panggilan darurat secara visual.

---

## ⚠️ Troubleshooting (Solusi Masalah)

**Q: Muncul pesan error `OpenCV: not authorized to capture video` atau `[FATAL ERROR] Kamera tidak dapat diakses`?**
**A:** macOS memblokir akses kamera untuk Terminal Anda dengan alasan privasi. Buka **System Settings** > **Privacy & Security** > **Camera**, lalu pastikan saklar (*toggle*) untuk aplikasi Terminal Anda (bisa berupa Terminal bawaan, iTerm, atau VSCode) telah diaktifkan/berwarna biru.

**Q: Program *lagging* atau error gagal resolve URL (misal: `Failed to resolve 'server.swadexi.com'`)?**
**A:** Ini berarti server API `swadexi.com` sedang mati (*down*), atau tidak dapat dijangkau dari koneksi internet Anda. Program akan tetap berjalan, tapi akan mencetak *error request* di layar terminal. Silakan ganti `URL_SERVER` di dalam `final.py` dengan URL *backend* atau server lokal yang sedang aktif.

## 🤝 Kontribusi
Dipersembahkan oleh tim **UROTERA** Institut Teknologi Sumatera.
