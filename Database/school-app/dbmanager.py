import mysql.connector
from datetime import datetime
from connection import connection
from Student import Student
from Teacher import Teacher
from Class import Class

class DbManager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def getStudentById(self,id):
        sql = "Select * from students where Id = %s"
        values = (id,)
        self.cursor.execute(sql,values)
        try:
            obj = self.cursor.fetchone()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print('Error:', err)

    def getStudentsByClassId(self,classid):
        sql = "Select * from students where ClassId = %s"
        values = (classid,)
        self.cursor.execute(sql,values)
        try:
            obj = self.cursor.fetchall()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print('Error:', err)
        
    def addStudent(self,student:Student):
        sql = "INSERT INTO students(Number,Name,Surname,Birthdate,Gender,ClassId) VALUES (%s,%s,%s,%s,%s,%s)"
        values = (student.number,student.name,student.surname,student.birthdate,student.gender,student.classid)
        self.cursor.execute(sql,values)
        
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt eklendi")
        except mysql.connector.Error as err:
            print(f"hata: {err}")

    def editStudent(self,student:Student):
        sql = "Update students set Number=%s,Name=%s,Surname=%s,Birthdate=%s,Gender=%s,ClassId=%s where Id = %s"
        values = (student.number,student.name,student.surname,student.birthdate,student.gender,student.classid,student.id)
        self.cursor.execute(sql,values)
        
        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt güncellendi.')
        except mysql.connector.Error as err:
            print('hata:', err) 

    def deleteStudent(self,studentid):
        sql = "delete from students where Id=%s"
        value = (studentid,)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt silindi.')
        except mysql.connector.Error as err:
            print('hata:', err)

    def getClasses(self):
        sql = "Select * from class"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Class.CreateClass(obj)
        except mysql.connector.Error as err:
            print('Error:', err)


    def addTeacher(self,teacher:Teacher):
        pass

    def editTeacher(self,teacher:Teacher):
        pass

db = DbManager()
# student = db.getStudentsByClassId(3)
# for i in student:
#     print(i)
