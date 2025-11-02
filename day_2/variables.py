# #day2 github
# first_name = "deniz" #str
# surname = "suzgen" #str
# full_name = "deniz suzgen" #str
# country = "turkey" #str
# city = "istanbul" #str
# age = 18 #int
# year = 2025 #int
# is_married = False #bool
# is_true = True #bool
# is_light_on = True #bool
# first_name, surname, age = "deniz", "suzgen", 18 #list
# print(type([first_name,surname,age]))
# print(len(first_name))
# liste = (first_name, surname)
# print(type(liste)) #tuple
# print(len(liste)) #2
# print(len(first_name), len(surname)) #5 6
# num_1 = 5
# num_2 = 4
# total = num_1 + num_2
# diff = num_1 - num_2
# product = num_2*num_1
# division = num_1/num_2
# remainder = num_2%num_1 #bölmeden kalanı hesaplar
# exp = num_1**num_2
# floor_division = num_1//num_2 #bölümü hesaplar (kalan atıldı)
# yaricap = input("yaricapi giriniz:")
# r = int(yaricap)
# pi = 3.14
# area_of_circle = pi*(r)**2
# circum_of_circle = 2*pi*r
# print("dairenin alanı: ", area_of_circle,'dairenin cevresi: ', circum_of_circle)
# alan = pi*r**2
# print("tam alan %.3f" %(alan))

# isim = input("adiniz")
# yaş = input("yaş")
# burç = input("burç")
# # karakter = {isim, yaş, burç} #bu fornat "set"
# karakter = {"isim": isim, "yaş": yaş, "burç": burç}
# print(karakter)
from threading import Thread
import random
import time
class Konum(Thread):
    def __init__(self):
        super().__init__()
        self.x = 5
        self.y = 7
        self.z = 10
    def değişim(self):
        artı = random.choice([-1, 0, 1])
        self.x += artı
        self.y += artı
        self.z += artı
        return f"koordinatlar (x,y,z): {self.x},{self.y},{self.z}"

konum = Konum()
konum.start()   