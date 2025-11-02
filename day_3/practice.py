age = "18"          #tirnak koyunca str oluo
age = int(age)
print(type(age))    #integer
height = 1.68
print(type(height)) #float
complex_number = 1 + 3j
print(type(complex_number)) #complex
taban = float(input("taban uzunluğu"))
print(type(taban)) #float
yükseklik = input("dikme uzunluğu")
taban = float(taban)
yükseklik = float(yükseklik)
print("üçgenin alani: ",taban*yükseklik*1/2) #float ve int arasi islem var str ile yok
kenar_a = int(input("Enter side a: "))
kenar_b = int(input("Enter side b: "))
kenar_c = int(input("Enter side c: "))
print("ucgenin cevresi = ", kenar_a+kenar_b+kenar_c)
#######
x = float(input("x degeri giriniz"))
print(type(x)) #float

y = x**2 + 6*x + 9
print("oordinat : ", y)

print(len("dragon") !=  len("python"))            #False
print( "on" in "python" and "on" in "dragon")     #True
print("jargon" in "hgfkukfyfjargon")              #True
print(not("on" in "python" and "on" in "dragon")) #False
lengthint = len("python")
print(type(lengthint)) #int
lenghtfloat = float(lengthint)
print(lenghtfloat)
lenghtstr = str(lenghtfloat)
print(lenghtstr)
print( 7/3 is 2.7)

##############################################################################FENA Bİ KOD BU################
sayi = input("sayi giriniz: ")
sayi = float(sayi)
if sayi == int:
    if sayi%2 == 0:
        print(sayi, " çifttir")
    else:
        print(sayi, " tektir")
else:
    print(sayi, " tam sayi deildir")

print(type("10") is type(10)) #False
print(int(9.8)is 10)          #False
print(int(10.8)is 10)         #True
print(type(int(10.8))) #int


for i in range(1,5):
    for j in range(1,5):
        print(i*j, end=" ")
    print(end="\n") #\n yeni satira gec demek

print("hello\ntatlisko") #sonraki satıra geçildi 
print("""sonraki satir   
sonraki satir""")        #"""sonraki satır\nsonraki satır çıktısı
isim = "deniz"
soyad = "süzgen"
space = " "
tam_ad = isim + space + soyad
print(tam_ad) #deniz süzgen
print(len(tam_ad)) #12(str)
print("deniz\nsüzgen") #########
print("deniz\tsüzgen") #########
print("deniz\\süzgen")
print("deniz\'süzgen")
print("deniz\"süzgen")

print("\thaftalar\t1\t2\t3\t4")
print("\ngünler")
print("pzt\t\t\tmat\ting\ting\ttarih")
print("salı\t\t\tsos\tedb\tfizik\ting")
print("çrş\t\t\tfizik\tkimy\tbio\tedb")
print("prş\t\t\tbio\ting\tfizik\tmat")
print("cum\t\t\tmat\tbio\tmat\ting")
print("haftasonu\t\t\t\\TATİL#############\"\'")

