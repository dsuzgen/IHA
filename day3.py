# #ctrl + k sonra ctrl + c # ekleme
# #ctrl + k sonra ctrl + u


# #kartezyen alan ÇALISMADI
import math
x3, y3 = input("kose 1")
x4, y4 = int(input("kose 2"))
x5, y5 = int(input("kose 3"))
alan = abs(((x4*y3)+(x5*y4)+(x3*y5)-(x3*y4)-(x4*y5)-(x5*y3))/2)
#DENEME 2 5. GÜNDEN
x1 = int(input("x1 değeri giriniz"))
y1 = int(input("y1 değeri giriniz"))
x2 = int(input("x2 değeri giriniz"))
y2 = int(input("y2 değeri giriniz"))
x3 = int(input("x3 değeri giriniz"))
y3 = int(input("y3 değeri giriniz"))
alan = abs(((x2*y3)+(x3*y2)+(x3*y3)-(x1*y2)-(x2*y3)-(x3*y3))/2)
print(alan)
x_koordinatlari = (x1, x2, x3)
y_koordinatlari = (y1, y2, y3)
kose = list(zip(x_koordinatlari, y_koordinatlari))
print("üçgenin köşeleri =", kose)


# #degiskene bagli mesafe ÇALIŞTI
import math
x1 = int(input("x1 i giriniz"))
y1 = int(input("y1 i giriniz"))
x2 = int(input("x2 yi giriniz"))
y2 = int(input("y2 yi giriniz"))
mesafe = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("uzaklık = ",mesafe)

#day2 pdf
print("hello","hi","hallo")
#print(len("hello","hallo")) #len tek değişken kabul edio
print(len("hallo")) #bu olur karakter sayısını verio => 5
is_married = False
print("married",is_married)
print(is_married)
print(type(1 + 1j)) #complex
print(type([1,2,3,4])) #list
print(type({"abc":"klm"})) #dictionary
print(type((1,2))) #tuple?
print(type(zip([1,2],(3,4)))) #zip?
print(zip([1,2],[3,4]))
print(str(10))
num_int = 10
print(num_int)
num_str = str(num_int)
print(num_str)