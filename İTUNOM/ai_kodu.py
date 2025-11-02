# import socket
# import json 
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.bind(("127.0.0.1", 9999))
# print("yer kontrol ist başlatıldı")
# while True:
#     data, addr = sock.recvfrom(1024)
#     telemetry = json.loads(data.decode())
#     print(f"gelen telemetri: {telemetry}")

import threading
from threading import Thread
from time import sleep
import random
import json
import socket
try:
    import cv2  # OpenCV yüklü değilse yorum satırı yapabilirsin
except Exception:
    cv2 = None
# --- KONUM CLASS ---
class Konum(Thread):
    def __init__(self):
        super().__init__()
        self.x = 5
        self.y = 7
        self.z = 10
        self.running = True

    def run(self):
        while self.running:
            art = random.choice([-1, 0, 1])
            self.x += art
            self.y += art
            self.z += art
    def durdur(self):
        self.running = False

    def durdur(self):
        pass
# --- İHA SIMÜLATÖRÜ CLASS ---
class IHASimulator(Thread):
    def __init__(self, KONUM, İRTİFA, KAMERA):
        super().__init__()
        self.KONUM = KONUM
        self.İRTİFA = İRTİFA
        self.KAMERA = KAMERA
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.target = ("127.0.0.1", 9999)

    def run(self):
        for _ in range(5):  # 5 defa veri gönderelim
            telemetry = {
                "x": self.KONUM.x,
                "y": self.KONUM.y,
                "z": self.KONUM.z,
                "irtifa": self.İRTİFA,
                "pil": random.randint(50, 100),
                "kamera": self.KAMERA
            }
            mesaj = json.dumps(telemetry)
            print("JSON Paket:", mesaj)

            # UDP gönderimi (gerçek bağlantı olmasa da)
            self.sock.sendto(mesaj.encode(), self.target)

            # Görüntü işlemede optimizasyon simülasyonu
            if cv2 is not None:
                try:
                    cap = cv2.VideoCapture(0)
                    ret, frame = cap.read()
                    if ret:
                        print("Kamera verisi alındı (1 kare).")
                    cap.release()
                except Exception:
                    print("Kamera modülü bulunamadı, simüle edildi.")
            else:
                print("Kamera modülü bulunamadı, simüle edildi.")
            sleep(2)


# --- ANA KISIM ---
konum = Konum()
konum.start()

iha = IHASimulator(konum, 100, "kamera_1.png")
iha.start()

iha.join()
konum.durdur()
konum.join()
