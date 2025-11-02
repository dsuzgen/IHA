def my_function(): #fonksiyon tanımlama
    isim = input("isim")
    print(isim)
my_function()

def greeting():
    print("merhaba")
greeting()

def greeting_1():
    return "merhaba"
greeting_1()           #hiçbi çıktısı yok
print(greeting_1())    #merhaba çıktısı var

def greeting_2():
    print("sm")
greeting_2()           #sm çıktısı var 

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_age(self):
        return self.age




köpek1 = Dog("karabaş", 5)
print(köpek1.get_age())
köpek2 = Dog("boncuk", 3)

##################################

class Car:
    def __init__(self, marka, model, yıl):
        self.marka = marka
        self.model = model
        self.yıl = yıl
    def get_info(self):
        print(f"{self.marka} {self.model} {self.yıl}") #değeri çıktı alır sonra değer kaybolur
araba1 = Car("Toyota", "Corolla", 2020)
araba2 = Car("Honda", "Civic", 2019)
araba1.get_info()

class Car:
    def __init__(self, marka, model, yıl):
        self.marka = marka
        self.model = model
        self.yıl = yıl
    def get_info(self):
        return f"{self.marka} {self.model} {self.yıl}" #değeri saklar çıktı almaz ondan print lazım
araba1 = Car("Toyota", "Corolla", 2020)
araba2 = Car("Honda", "Civic", 2019)
print(araba1.get_info())
print(araba2.get_info())

class BankAcc:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return f"yeni para = {self.balance}"
    def withdraw(self, amount):
        if amount > self.balance:
            return "yetersiz bakiye"
        else:
            self.balance -= amount
            return f"hesabınızdan {amount} tl kadar para çekildi. kalan para = {self.balance}"
    def get_balance(self):
        return self.balance

hesap1 = BankAcc("deniz", 1000)
print(hesap1.withdraw(15))
print(hesap1.get_balance())


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)

    def get_average_grade(self):
        return sum()



s1 = Student("deniz", 85)
s2 = Student("ayşe", 90)
s3 = Student("ömer", 78)
course = Course("Matematik")
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)
average_grade = course.get_average_grade()
