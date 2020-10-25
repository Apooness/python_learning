# 5- Aşağıdaki güncelleme sorularını yapınız.
#   b- cinsiyet' e göre aldığınız bir öğrencinin bilgilerini güncelleyiniz.

import mysql.connector
from datetime import datetime
from connection import connection

class Student:
    connection = connection
    mycursor = connection.cursor()

    def __init__(self,id,studentNumber,name,surname,birthdate,gender):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender

    def saveStudent(self):
        sql = "INSERT INTO students(Number,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
        values = (self.studentNumber,self.name,self.surname,self.birthdate,self.gender)
        Student.mycursor.execute(sql,values)
        
        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt eklendi")
        except mysql.connector.Error as err:
            print(f"hata: {err}")
        finally:
            Student.connection.close()
   
    @staticmethod
    def saveStudents(students):
        sql = "INSERT INTO students(Number,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
        values = students
        Student.mycursor.executemany(sql,values)
        
        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt eklendi")
        except mysql.connector.Error as err:
            print(f"hata: {err}")
        finally:
            Student.connection.close()
   
    @staticmethod
    def StudentInfo():
        sql = "Select * from students where Gender = 'K' Order By Name"
        Student.mycursor.execute(sql)
        result = Student.mycursor.fetchall()
        # print(f"{result[0][0]} tane erkek öğrenci vardır.")
        for i in result:
            print(i)
   
    @staticmethod
    def GetStudentById(id):
        sql = "Select * from students where Id = %s"
        vaules = (id,)
        Student.mycursor.execute(sql,vaules)
        result = Student.mycursor.fetchone()
        return (Student(result[0], result[1], result[2], result[3], result[4], result[5]))
    
    def UpdateStudent(self):
        sql = "Update students set Number=%s,Name=%s,Surname=%s,Birthdate=%s,Gender=%s where Id=%s"
        values = (self.studentNumber,self.name,self.surname,self.birthdate,self.gender,self.id)
        Student.mycursor.execute(sql,values)
        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt güncellendi')
        except mysql.connector.Error as err:
            print('Hata:',err)

    @staticmethod
    def UpdateStudents(liste):
        sql = "update students set Number=%s,Name=%s,Surname=%s,Birthdate=%s,Gender=%s where Id = %s"
        values = []
        order = [1,2,3,4,5,0]

        for item in liste:
            item = [item[i] for i in order]
            values.append(item)

        Student.mycursor.executemany(sql,values)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt güncellendi')
        except mysql.connector.Error as err:
            print('Hata:',err)
    
    @staticmethod
    def GetStudentByGender(gender):
        sql = "Select * from students where Gender = %s"
        vaules = (gender,)
        Student.mycursor.execute(sql,vaules)
        return Student.mycursor.fetchall()

    @staticmethod
    def GetStudent():
        sql = "Select students.Number,students.Name,students.Surname,genders.gender From students inner join genders on genders.id = students.Gender"
        Student.mycursor.execute(sql)
        result = Student.mycursor.fetchall()
        return result

    @staticmethod
    def DeleteInfo():
        sql = "Delete from students where name = '%Mr%'"
        Student.mycursor.execute(sql)
        Student.connection.commit()


# students = Student.GetStudentByGender("E")
# liste = []
# for i in students:
#     i = list(i)
#     i[2] = "Mr "+ i[2]
#     liste.append(i)
# Student.UpdateStudents(liste)

students = Student.GetStudent()
for std in students:
    print(std)