from dbmanager import DbManager
from Student import Student
import datetime

class App:
    def __init__(self):
        self.db = DbManager()
    
    def initApp(self):
        msg = "*****\n1-Öğrenci Listesi\n2-Öğrenci Ekle\n3-Öğrenci Güncelle\n4-Öğrenci Sil\n5-Öğretmen Ekle\n6-Sınıflara Göre Dersler\n7-Çıkış(E/Ç)"
        while True:
            print(msg)
            secim = input("Seçim: ")
            if secim == "1":
                self.displayStudents()
            elif secim == "2":
                self.addStudent()
            elif secim == "3":
                self.editStudent()
            elif secim == "4":
                self.deleteStudent()
            else:
                break

    def addStudent(self):
        self.displayClasses()
        classid = int(input("Hangi sınıfa bakmak istiyorsunuz?: "))
        number = int(input("Okul numarası: "))
        name = input("Ad: ")
        surname = input("Soyad: ")
        year = int(input("Doğum yılı: "))
        month = int(input("Doğum ayı: "))
        day = int(input("Doğum günü: "))
        birthdate = datetime.datetime(year,month,day)
        gender = input("Cinsiyet: ")

        student = Student(None,number,name,surname,birthdate,gender,classid)
        self.db.addStudent(student)

    def editStudent(self):
        classid = self.displayStudents()
        studentid = int(input("Hangi öğrenci: "))

        student = self.db.getStudentById(studentid)

        student[0].name = input("Ad: ") or student[0].name
        student[0].surname = input("Soyad: ") or student[0].surname
        student[0].gender = input("Cinsiyet: ") or student[0].gender
        student[0].classid = int(input("Sınıf id: ")) or student[0].classid
        year = int(input("Doğum yılı: "))
        month = int(input("Doğum ayı: "))
        day = int(input("Doğum günü: "))
        student[0].birthdate = datetime.datetime(year,month,day) or student[0].birthdate
        self.db.editStudent(student[0])

    def displayClasses(self):
        classes = self.db.getClasses()        
        for c in classes:
            print(c.id,"-",c.name)

    def deleteStudent(self):
        classid = self.displayStudents()
        studentid = int(input("Hangi öğrenci: "))
        
        self.db.deleteStudent(studentid)

    def displayStudents(self):
        self.displayClasses()
    
        classid = int(input("Hangi sınıfa bakmak istiyorsunuz?: "))
        students = self.db.getStudentsByClassId(classid)
        print("Öğrenci Listesi:")
        for std in students:
            print(f'{std.id}-{std.name} {std.surname}')
        return classid
app = App()
app.initApp()