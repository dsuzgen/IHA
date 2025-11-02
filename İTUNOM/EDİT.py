class Student:
    def __init__(self, name, puan):
        self.name = name
        self.puan = puan

class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        def not_ortalaması(self):
        value = 0
        for student in self.students:
            value += student.puan
        return value / len(self.students)

s1 = Student("Ali", 85)
s2 = Student("Ayşe", 90)
s3 = Student("Mehmet", 78)
course = Course("Mat")
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)


   



 

