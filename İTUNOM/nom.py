from threading import Thread  #eşzamanlı çalıştırmak için konum ve irtifa msl aynı anda
from time import sleep        #düzenli aralıklarla olştrurmak için
import time
import random

konum = [10, 10]
irtifa = 100
def h():
    global irtifa
    while True:
        for _ in range(5):
            irtifa += random.choice([-1, 0, 1])
            print(f"İrtifa: {irtifa} metre")
            time.sleep(1)
def k():
    global konum
    while True:
        for _ in range(5):
            konum[0] += random.choice([-1, 0, 1])
            konum[1] += random.choice([-1, 0, 1])
            print(f"Konum: {konum}")
            time.sleep(1)

if __name__ == "__main__":
    irtifa_thread = Thread(target=h)
    konum_thread = Thread(target=k)
    
    irtifa_thread.start()
    konum_thread.start()

# class robot():       #alttaki yönteme göre daha gelişmiş manuel girme yükünü
#     def __init__(self, name, color, weight):
#         self.name = name
#         self.color = color
#         self.weight = weight

#     def introduceself(self):
#         print(f"adım: {self.name}, rengim: {self.color}, ağırlığım: {self.weight} kg")

# r1 = robot("tom", "red", 30)
# r2 = robot("jerry", "blue", 40)
# r1.introduceself()
# r2.introduceself()

# class Robot():
#     def introduce_self(self):
#         print("adım:" + self.name + ", rengim: " + self.color + ", ağırlığım: " + str(self.weight))
# robot1 = Robot()
# robot1.name = "danny"
# robot1.color = "yellow"
# robot1.weight = 35.5
# robot1.introduce_self()
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