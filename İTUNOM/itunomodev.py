#İLK YAPTIĞIM BEĞENMEDİĞİM VERSİYONDU#
# from threading import Thread  #eşzamanlı çalıştırmak için konum ve irtifa msl aynı anda
# from time import sleep        #düzenli aralıklarla olştrurmak için
# import random
# import json
# h = 100
# def yükseklik():
#     ekleme = random.choice([-1, 0, 1])
#     global h
#     h += ekleme
#     return h
# from threading import Thread
# from time import sleep    
# import random

# class Konum(Thread):
#     def __init__(self):
#         super().__init__()
#         self.x = 5
#         self.y = 7
#         self.z = 10
#         self.running = True
    
#     def run(self):                          #run fonks bak
#         for _ in range (3):
#             artı = random.choice([-1, 0, 1])
#             self.x += artı
#             self.y += artı
#             self.z += artı
#             a = '{"koordinatlar (x,y,z)": {self.x},{self.y},{self.z}}'
#             b = json.loads(a)
#             print(["koordinatlar (x, y, z)"]) #returnle tek çıktı oluor printle her değişimde çıktı alır
#             sleep(0.5)
#         def durdur(self):
#             self.running = False

   

# class IHASimulator(Thread): #parent class threadden miras  #ÇIKTI ALMA KODU
#     def __init__(self, KONUM, İRTİFA, KAMERA):
#         super().__init__()
#         self.KONUM = KONUM
#         self.İRTİFA = İRTİFA    
#         self.KAMERA = KAMERA
    
#     def run(self): #threadin çalıştıracağı method
#         for _ in range(3):
#             print(f"Konum: {self.KONUM.x}, {self.KONUM.y}, {self.KONUM.z}\nİrtifa: {self.İRTİFA}\nKamera Görüntüsü: {self.KAMERA}\n------------")
#             sleep(0.5)
# konum = Konum()
# konum.start()
# iha = IHASimulator(konum, 100, "Görüntü_1.png")
# iha.start() 
# iha.join()
# konum.durdur()
# konum.join()

 

from threading import Thread
from time import sleep
import random
import json

# Konum değişimi için ayrı bir thread
class Konum(Thread):
    def __init__(self):
        super().__init__()
        self.x = 5
        self.y = 7
        self.z = 10


    def run(self):
        # Sürekli konumu değiştir
        for _ in range(5):
            self.değişim()
            sleep(0.5)

    def değişim(self):
        artı = random.choice([-1, 0, 1])
        self.x += artı
        self.y += artı
        self.z += artı
        print(f"Yeni koordinatlar (x, y, z): ({self.x}, {self.y}, {self.z})")

# İHA simülasyonu sınıfı
class IHASimulator(Thread):
    def __init__(self, konum, irtifa, kamera):
        super().__init__()
        self.konum = konum
        self.irtifa = irtifa
        self.kamera = kamera
       
    def run(self):
        # İHA verilerini düzenli olarak "yer kontrol istasyonuna" gönderir gibi simüle et
        c = {
            "konum": {self.konum.x, self.konum.y, self.konum.z},
            "irtifa": self.irtifa,
            "kamera görüntüsü": self.kamera
        }
        j = json.dumps(c, ensure_ascii=False, indent=2)
        print("\nVERİ\n", j)
        d = json.loads(j)
        for _ in range(5):
            print(f"konum: {d["konum"]}")
            print(f"irtifa: {d["irtifa"]}")
            print(f"kamera görüntüsü: {d["kamera görüntüsü"]}")
            print("------------")
            sleep(0.5)



# Ana program
if __name__ == "__main__":
    # Konum thread'ini başlat
    konum_thread = Konum()
    konum_thread.start()

    # İHA simülasyonunu başlat
    iha_thread = IHASimulator("5,7,10", 100, "Görüntü_1.png")
    iha_thread.start()

    # Her iki thread’in bitmesini bekle
    konum_thread.join()
    iha_thread.join()

    print("Simülasyon tamamlandı.")

    import cv2
print(cv2.__version__)
kamera = cv2.VideoCapture(0)
while True:
    ret, frame = kamera.read()
    if not ret:
        print("görüntü alınamadı")
        break
    cv2.imshow("canlı görüntü", frame)
    if cv2.waitKey(1) & 0xFF ==ord("q"):
        break
kamera.release()
cv2.destroyAllWindows


   



