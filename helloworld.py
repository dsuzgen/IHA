print(2+3)
print(2-3)
print(2*3)
print(2%3)
print(2/3)
print(2**3)
print(type('deniz'))
print(type("3.14"))
print(type(True))
print(type(1+2j))
"deniz"
print(type("deniz"))
#öklid hesaplama
import math
x1, y1 = 2, 4
x2, y2 = 5, 8
mesafe = math.sqrt((x2 - x1)**2 +(y2 - y1)**2)
print("uzaklık" , mesafe)
print(type(mesafe))
#kartezyen alan hesaplama
import math
x1, y1 = 0, 0
x2, y2 = 4, 0
x3, y3 = 2, 6
alan = abs(((x1 * y2 + x2 * y3 + x3 * y1)-(x2 * y1 + x3 * y2 + x1 * y3)) / 2)
print("alan=" , alan)

