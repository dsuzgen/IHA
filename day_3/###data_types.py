my_list = [1, "hello", "1", True, 1.2] #"()"koysaydim tuple oluo list
print(type(my_list[0]))  #int
print(type(my_list[1]))  #str
print(type(my_list[2]))  #str
print(type(my_list[3]))  #bool
print(type(my_list[4]))  #float
print(type(my_list))     #list
#
my_dict = {"isim": "deniz", "yaş": 18, "burç": "balik", "is_happy": None}
print(my_dict["is_happy"])
print(my_dict["isim"])
print(my_dict["yaş"])
print(my_dict["burç"])
my_list[1] = "bye"
print(my_list[1])        #bye (2.girdisi hellodan bye yapıldı)
my_dict[0] = "murtaza"
print(my_dict[0])        #isim murtaza yapildi
#
my_tuple = (10, 20, 30)
# my_tuple(0) = 20       #hata verir tuple fonks immutable(deiştirilemez)
print(my_tuple[0])       #10
print(type(my_tuple[1])) #int
#
#zip
isimler = ["Led", "Amy", "Deniz"]
soyisimler = ["Zeppelin", "Winehouse", "Süzgen"]
print(isimler[1])        #Amy
zip_formati = list(zip(isimler, soyisimler)) #liste bu zip deil
print(type(zip_formati)) #list
print(list(zip_formati)) #[('Led', 'Zeppelin'), ('Amy', 'Winehouse'), ('Deniz', 'Süzgen')]
print("fav insanlarim:", list(zip_formati)) #zip sdc liste birleştirmede görevli ayrı bir ögeyi tek başına çağıramazsın
#print(zip(isimler, soyisimler)) çalışmaz ki??!! zip sdc eşleme printe çağıramazsın listesini çağırırsın 
# liste_formati = list(zip(isimler, soyisimler)) bu gereksiz ztn liste formatında zip_formati is liste_formati
print("en sevdiim:", zip_formati[2]) #list diy ayrı çağırılabiliyor


