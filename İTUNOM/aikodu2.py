import threading       #aynanda birdn fazlaiş
import socket          #udp ve tcp verileri iletimi
import json            #veriyi hem pc hem insan okuyabilsin diye
import cv2             #kamera için
from time import sleep #bekleme

# === YER KONTROL İSTASYONU SINIFI ===
class YerKontrolIstasyonu:
    def _init_(self, ip="127.0.0.1", port=9999):
        self.ip = ip
        self.port = port
        self.telemetri_thread = threading.Thread(target=self.telemetri_al) #aynanda çalışabilio
        self.goruntu_thread = threading.Thread(target=self.goruntu_izle)  #aynanda çalışabilio
        self.running = True

    # --- Telemetri Verisini Dinleyen Thread ---
    def telemetri_al(self): #udpden gelen json u okur
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((self.ip, self.port))
        print(f"[YKİ] Telemetri dinleme başladı ({self.ip}:{self.port})")

        while self.running: #yki açık olduğu sürece aslında
            data, addr = sock.recvfrom(1024) #1024 bayt veri alma
            telemetry = json.loads(data.decode())
            self.telemetri_goster(telemetry)

    # --- Telemetriyi Ekranda Gösteren Fonksiyon ---
    def telemetri_goster(self, telemetry):
        print("\n--- Gelen Telemetri Verisi ---")
        print(f"X: {telemetry['x']} | Y: {telemetry['y']} | Z: {telemetry['z']}")
        print(f"İrtifa: {telemetry['irtifa']} | Pil: %{telemetry['pil']}")
        print(f"Kamera: {telemetry['kamera']}")
        print("-------------------------------")

    # --- Görüntü Akışını Gösteren Thread ---
    def goruntu_izle(self):
        print("[YKİ] Görüntü akışı başlatıldı.")
        cap = cv2.VideoCapture(0)  # 0: Bilgisayarın kamerası
        while self.running:
            ret, frame = cap.read()
            if ret:
                cv2.imshow("YKİ - Canlı Görüntü", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.running = False
                break
        cap.release()
        cv2.destroyAllWindows()

    # --- Çalışmayı Başlat ---
    def baslat(self):
        self.telemetri_thread.start()
        self.goruntu_thread.start()

    # --- Durdur ve Temizle ---
    def durdur(self):
        self.running = False
        self.telemetri_thread.join()
        self.goruntu_thread.join()
        print("[YKİ] Sistem kapatıldı.")


# === ANA PROGRAM ===
if __name__ == "_main_":
    yki = YerKontrolIstasyonu()
    yki.baslat()

    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        yki.durdur()