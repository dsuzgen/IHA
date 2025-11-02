liste_1 = []
liste_2 = ["deniz", "tolga", "devrim", "kaya", "süzgen", "ayşe", "ömer"]
print(len(liste_2)) #7
uzunluk = len(liste_2)
print("birinci eleman =", liste_2[0]) 
print("ortanca eleman =", liste_2[uzunluk//2])
print("son eleman =", liste_2[-1])
mixed_data_types = ["deniz", 18, 1.68, False, "istanbul"]
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print("the num of comp in list is", len(it_companies))
print(it_companies[0])
print(it_companies[-1])
print(it_companies[len(it_companies)//2])
it_companies.remove("Microsoft")
it_companies.insert(2, "Meta")
print(it_companies)
it_companies.insert(7,"Twitter")
it_companies.insert((len(it_companies))//2, "Linkedin")
print(len(it_companies)) #9
print(it_companies) #['Facebook', 'Google', 'Meta', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Twitter', 'Linkedin']
sira = int(input("hangi sıradki şirketi seçiyorsunuz:"))
if sira-1 in range(0,9):
    if sira-1 == 4 is True:
        print("kelime ztn büyük harfli")
    else:
        it_companies[sira-1] = it_companies[sira-1].upper() #title halinde ztn ya upper olcak ya lower
        print(it_companies)
else:
    print("hatalı sıra girdiniz")

print("#; ".join(it_companies)) #join append inert gibi kalıcı değiştirmez sadece yazdırır ondan printle kullanılır
şirket = input("şirket adı giriniz ")
if şirket.title() in it_companies or şirket.capitalize() in it_companies or şirket.upper() in it_companies:
    print(şirket.title(), "şirketi listede var")
else:
    print("şirket listede yok")
it_companies.sort() #kalıcı değişiklik yapar alfabetik sıralar
print(it_companies) #alfabetik sıralandı
it_companies.sort(reverse=True) #Z den A ya sıralar
print(it_companies) #Z den A ya sıralandı
del it_companies[0:3] #ilk 3 elemanı siler #BUKADAR ABİ KENDİM AKIL ETTİM 
#liste artık 6 elemanlı
del it_companies[-1:-4] #son 3 elemanı siler
print(it_companies) #['IBM', 'Google', 'Facebook']
it_companies.remove("Google")
it_companies = ['Facebook', 'Google', 'Meta', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Twitter', 'Linkedin']
del it_companies[0]
print(it_companies) #ilk eleman silindi
del it_companies[3:5]
del it_companies[-1]
del it_companies[:] #tüm elemanları siler ##############
it_companies.clear() #tüm elemanları siler
print(it_companies) #boş liste çıktı []
del it_companies #listeyi komple siler
# print(it_companies) #hata verir liste yok çünkü silindi
front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "MongoDB"]
#front_end.join(back_end) #çalışmama nedeni: join liste metodu değil string metodudur
full_stack = front_end + back_end
full_stack.insert(4, "Python")
full_stack.insert(5, "SQL")
print(full_stack) #['HTML', 'CSS', 'JS', 'React', 'Python', 'SQL', 'Redux', 'Node', 'Express', 'MongoDB']
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(max(ages)) #26
print(min(ages)) #19
ages.append(min(ages))
ages.append(max(ages))
ages.sort()
print(ages) # 12 öğe #[19, 19, 19, 20, 22, 24, 24, 24, 25, 25, 26, 26]
sayi = int(len(ages)) #12
if sayi % 2 == 0:
    print(int((ages[int((sayi/2)-1)] + ages[int(sayi/2)])/2), "medyan değeridir") #doğrusu 
else:
    print(ages[int(sayi//2)], "medyan değeridir")
