#!/usr/bin/env python3
import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import requests
import time
import os
import urllib.request

# ==========================================
# KONFIGURASI APLIKASI
# ==========================================
URL_SERVER = "http://server.swadexi.com/up/iot2.php"
NOMOR_RUANG = 102
COOLDOWN_SECONDS = 3 # Waktu jeda (detik) sebelum bisa kirim kode yang sama lagi

# ==========================================
# INISIALISASI MEDIAPIPE HANDS (NEW TASKS API)
# ==========================================
# Karena Mac M1/M2/M3 (ARM64) seringkali tidak memiliki submodul `solutions`, 
# kita gunakan API `Tasks` terbaru dari Google yang lebih stabil.

model_path = 'hand_landmarker.task'
if not os.path.exists(model_path):
    print("[INFO] Mengunduh model AI MediaPipe (sekali saja)...")
    url = 'https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task'
    urllib.request.urlretrieve(url, model_path)
    print("[INFO] Model berhasil diunduh!")

base_options = python.BaseOptions(model_asset_path=model_path)
options = vision.HandLandmarkerOptions(base_options=base_options, num_hands=1)
detector = vision.HandLandmarker.create_from_options(options)

# Daftar garis tulang tangan
HAND_CONNECTIONS = [
    (0,1), (1,2), (2,3), (3,4),
    (0,5), (5,6), (6,7), (7,8),
    (5,9), (9,10), (10,11), (11,12),
    (9,13), (13,14), (14,15), (15,16),
    (13,17), (17,18), (18,19), (19,20),
    (0,17)
]

def draw_landmarks(img, landmarks):
    h, w, _ = img.shape
    # Gambar garis
    for connection in HAND_CONNECTIONS:
        p1 = landmarks[connection[0]]
        p2 = landmarks[connection[1]]
        cv2.line(img, (int(p1.x * w), int(p1.y * h)), (int(p2.x * w), int(p2.y * h)), (0, 255, 0), 2)
    # Gambar titik
    for landmark in landmarks:
        cv2.circle(img, (int(landmark.x * w), int(landmark.y * h)), 4, (0, 0, 255), -1)

# ==========================================
# FUNGSI UNTUK MENGIRIM REQUEST KE SERVER
# ==========================================
last_sent_time = 0
last_sent_kode = 0

def send_request(kode):
    global last_sent_time, last_sent_kode
    current_time = time.time()
    
    # Mencegah pengiriman berulang-ulang tanpa jeda
    if current_time - last_sent_time > COOLDOWN_SECONDS or kode != last_sent_kode:
        try:
            url = f"{URL_SERVER}?ruang={NOMOR_RUANG}&kode={kode}"
            print(f"[INFO] Mengirim sinyal: {url}")
            response = requests.get(url, timeout=3)
            print(f"[SUCCESS] Respon Server: {response.status_code}")
            last_sent_time = current_time
            last_sent_kode = kode
            return True
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Gagal mengirim request: {e}")
            return False
    return False

# ==========================================
# FUNGSI MENGHITUNG JARI TERANGKAT
# ==========================================
def count_fingers(hand_landmarks, hand_label):
    tip_ids = [4, 8, 12, 16, 20]
    fingers = []

    # Jempol (X-axis)
    if hand_label == "Right":
        if hand_landmarks[tip_ids[0]].x < hand_landmarks[tip_ids[0] - 1].x:
            fingers.append(1)
        else:
            fingers.append(0)
    else: # Kiri
        if hand_landmarks[tip_ids[0]].x > hand_landmarks[tip_ids[0] - 1].x:
            fingers.append(1)
        else:
            fingers.append(0)

    # 4 Jari lainnya (Y-axis)
    for id in range(1, 5):
        if hand_landmarks[tip_ids[id]].y < hand_landmarks[tip_ids[id] - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers.count(1)

# ==========================================
# PROGRAM UTAMA
# ==========================================
def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("[FATAL ERROR] Kamera tidak dapat diakses. Pastikan kamera terhubung.")
        return

    print("[INFO] Aplikasi SMADER berjalan... Tekan 'ESC' untuk keluar.")

    while True:
        ret, img = cap.read()
        if not ret:
            print("[ERROR] Gagal membaca frame dari kamera.")
            break
            
        # Flip gambar secara horizontal agar seperti cermin
        img = cv2.flip(img, 1)
        
        # Konversi BGR ke RGB untuk MediaPipe
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Proses frame dengan MediaPipe Tasks API
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=img_rgb)
        detection_result = detector.detect(mp_image)

        fingers_count = 0
        kode = 0
        
        if detection_result.hand_landmarks:
            for i, hand_landmarks in enumerate(detection_result.hand_landmarks):
                # Pada Tasks API, label tersimpan di category_name (Right/Left)
                hand_label = detection_result.handedness[i][0].category_name
                
                # Gambar titik (landmarks) dan tulang tangan secara manual
                draw_landmarks(img, hand_landmarks)
                
                # Hitung jari
                fingers_count = count_fingers(hand_landmarks, hand_label)
                
                # Konversi jumlah jari ke kode
                if fingers_count == 2:
                    kode = 1
                elif fingers_count == 3:
                    kode = 2
                elif fingers_count == 4:
                    kode = 3
                elif fingers_count == 5:
                    kode = 4
                
                # Kirim request jika kode valid (1-4)
                if kode > 0:
                    status = send_request(kode)
                    if status:
                        cv2.rectangle(img, (0, 0), (img.shape[1], 50), (0, 200, 0), cv2.FILLED)
                        cv2.putText(img, f"KODE {kode} TERKIRIM!", (20, 35), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
                
        # Tampilkan teks informasi jumlah jari dan kode
        cv2.putText(img, f"Jari: {fingers_count} | Kode (Kirim): {kode}", (20, 450), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
        
        cv2.imshow('SMADER - MediaPipe Tasks API', img)

        # Tekan 'ESC' untuk keluar
        k = cv2.waitKey(1) & 0xff
        if k == 27: 
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()