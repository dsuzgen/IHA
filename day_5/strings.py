#tuple?
# %f %d %s
#####yeni tip
a = "deniz"
print(f"benim adim {a}")
r = 4
pi = 3.14
print(f"{r}*{pi} = {r*pi:.1f}") #4*3.14 = 12.6
print(f"{r}*{pi} = {r*pi:.3f}") #4*3.14 = 12.560
print("dairenin alanı {} * {}**2 = {:.2f}".format(pi, r, pi*r**2)) #50.24
print("dairenin alanı {} * {}**2 = {:.3f}".format(pi, r, pi*r**2)) #50.240

#####eski tip
isim = input("adınız")
yaş = int(input("yaş"))
boy = float(input("boyunuz"))
renk = input("fav renk")
print("""merhaba benim adim %s, yaşım %d 
boyum %.2f gözlerimin rengi %s""" %(isim, yaş, boy, renk))

liste = "deniz", "ayşe", "devrim"#tuple
liste = ("deniz", "ayşe", "devrim")#tuple
liste = ["deniz", "ayşe", "devrim"]#list
print(type(liste))
print(liste[2])

okul_no = input("okul numaraniz: ") #123456789
okul_no = "123456789"
bölüm_siralamasi = okul_no[-2:] #89
bölüm_siralamasi_1 = okul_no[:-1] #12345678
bölüm_siralamasi_2 = okul_no[::]
bölüm_siralamasi_3 = okul_no[-1::-2] #97531 -1 den başla 0 a kadar -2 karakterde git
bölüm_siralamasi_4 = okul_no[::-1] #987654321
bölüm_siralamasi_5 = okul_no[0:8:3] #0 başlangıç, 6 bitiş, 2 kaç karakterde bir alınacak indeksi
bölüm_siralamasi_6 = okul_no[::-2] #başl. ve bitiş belirtilmemiş -2 karakterde bir sondan başa
                                   #alıncak tersten 97531

print(bölüm_siralamasi) #89
print(bölüm_siralamasi_1) #12345678
print(bölüm_siralamasi_2) #123456789
print(bölüm_siralamasi_3) #97531
print(bölüm_siralamasi_4) #987654321
print(bölüm_siralamasi_5) #147
print(bölüm_siralamasi_6) #97531

dil = "python"
print(dil[2]) #t
#######
print("********")
isim = "deniz"
print(isim.capitalize()) #Deniz
print(isim.count("e")) #1
print(isim.count("a", 7,)) #0
print(isim.count("de")) #1
print(isim.endswith("iz")) #True
print(isim.endswith("ömer")) #False
# # isim = "de\tni\tz" 
# # print(isim) #8 boşluk bırakır
##print(isim.expandtabs(10)) #10 boşluk bırakır

#rfind
print(isim.rfind("y")) #-1 aratılan stringin ilk occurence ini bulur yoksa -1 çıktısı
print(isim.rfind("n")) #2
#print("alan" +  13) #çalışmaz sdc str ile bu çalışır
print("alan",  13) #çalışır yani #alan 13 
kisa = "iz"
#index
print(isim.index(kisa)) #3
#sub stringin ilk haneinin sırasını yazar
#rindex son hane sırası (en büyük sıra) => #4
#isalnum (is alphanumeric): abc, 0123
şifre = "De1527Su@"
print(şifre.isalnum()) #False @*# sayilmaz
parola = "de 1234 "
print(parola.isalnum()) #False boşluk
ad = "deniz1423"
print(ad.isalnum()) #True
#isalpha() checks if all alphabet (a-z / A-Z)
#isdecimal (0-9)
#isdigit (0-9 ve bazı abc dışı karakterler)
#isnumeric isdigiti kapsar ½ gibi şeyler de eklenio
#isidentifier string = valid variable mi kontrol
#islower lowercase
#isupper upcase
#join liste cümle###################_______________________ 
print("******")
listem = ["benim", "adım", "deniz"]
print(type(listem)) #list ama tupleyle de çalşıo
sonuç = "*".join(listem)
print(sonuç) #benim*adım*deniz
#strip verilen karakterlerin hepsini çıkarır
isim = "abülmecidhabib"
print(isim.strip("bia")) #ülmecidh
#replace
print(isim.replace("habib", "rezzak"))
#split splits string with given separator
challenge = "30, days, of, python"
print(challenge.split(", "))
#title baş harfleri büyütür
isim = "Adım deniz"
print(isim.title()) #Adım Deniz
#swapcase büyük harf to küçük küçük harf to büyük çevirir
#startswith verilenle mi başlio kontrol
print(isim.startswith("adım")) #False
print(isim.startswith("Adım")) #True
#SPLİT SEPARATOR ?????
