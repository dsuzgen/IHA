listem = ["deniz", "benim", "adım", "soyadım"]
birinci, ikinci, *rest = listem
print(rest) #adım
print(type(birinci)) #str
print(type(rest)) #list
print(len(rest)) #2
print(listem[1:3]) #['benim', 'adım'] 1 den başlayıp 3 e kadar 3 dahil değil
adım = "deniz" in listem
print(adım) #True
soyadım = "süzgen" in listem
print(soyadım) #False
listecik = ["tolga", "süleyman", "ömer"]
["tolga", "süleyman", "ömer"].append("deniz") #çalışmadı?###########################
print(listecik)
listecik.append("deniz")
print(listecik) #['tolga', 'süleyman', 'ömer', 'deniz']
listecik.insert(1, "devrim")
print(listecik)
