class Araba():
    def __init__(self, marka, model, beygir):
        self.marka = marka
        self.model = model
        self.beygir = beygir
    def özellik_yazdır(self):
        print(f"Marka: {self.marka}, Model: {self.model}, Beygir: {self.beygir} hp")
benim_arabam = Araba("Toyota", "Corolla", 130)
benim_arabam.özellik_yazdır()



class Araba():
    def __init__(self, marka, model, beygir):
        self.marka = marka
        self.model = model
        self.beygir = beygir
    def özellik_yazdır(self):
        print(f"Marka: {self.marka}, Model: {self.model}, Beygir: {self.beygir} hp")
benim_arabam = Araba("Toyota", "Corolla", 130)
benim_arabam.özellik_yazdır()
class Otobüs(Araba):
    pass
okul_otobüsü = Otobüs("Mercedes", "Sprinter", 160)
okul_otobüsü.özellik_yazdır()

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    capacity = 50
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)
school_bus = Bus("School Volvo", 180, 12)
print(school_bus.seating_capacity(capacity=50))


köpek_ayak = input("Köpeğin ayak sayısını giriniz: ")
tavuk_ayak = input("Tavuğun ayak sayısını giriniz: ")
yunus_ayak = input("Yunusun ayak sayısını giriniz: ")
class Animal:
    def __init__(self, name, species, canlı = "canlı"):
        self.name = name
        self.species = species
        self.canlı = canlı

    def ayak_sayısı(self, legs):
        return f"{self.species} türüne ait {self.name} isimli hayvanın {legs} ayağı vardır.ve bu bir {self.canlı}dır"
    
class Dog(Animal):
    def ayak_sayısı(self, legs=4):
        return super().ayak_sayısı(legs= köpek_ayak)
class Chicken(Animal):
    def ayak_sayısı(self, legs=2):
        return super().ayak_sayısı(legs= tavuk_ayak)
    
class dolphin(Animal):
    def ayak_sayısı(self, legs=0):
        return super().ayak_sayısı(legs= yunus_ayak)
dog = Dog("zeytin", "köpek")
chicken = Chicken("küllü", "tavuk")
dolphin = dolphin("dori", "yunus")
print(dog.ayak_sayısı())
print(chicken.ayak_sayısı())
print(dolphin.ayak_sayısı())

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        return self.capacity * 100 * 1.1

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())
print(isinstance(School_bus, Bus))     #True
print(issubclass(Bus, Vehicle))        #True
print(isinstance(School_bus, Vehicle)) #True
