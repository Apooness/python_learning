from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QLineEdit
import sys
import mysql.connector

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Database Connect")
        self.setGeometry(100,100,500,500)
        self.InitUI()
        self.ConnectDb()
    def InitUI(self):

        self.lineEdit1 = QLineEdit(self)
        self.lineEdit1.setPlaceholderText("Enter Your Name")
        self.lineEdit1.setGeometry(100,100,200,30)

        self.lineEdit2 = QLineEdit(self)
        self.lineEdit2.setPlaceholderText("Enter Your Email")
        self.lineEdit2.setGeometry(100,150,200,30)

        self.lineEdit3 = QLineEdit(self)
        self.lineEdit3.setPlaceholderText("Enter Your Phone")
        self.lineEdit3.setGeometry(100,200,200,30)

        self.button = QPushButton("Insert Data to Database",self)
        self.button.move(100,250)
        self.button.resize(150,50)
        self.button.clicked.connect(self.InsertData)

        self.show()

    def ConnectDb(self):
        self.connection = mysql.connector.connect(host="localhost",user="root",password="123456A789a",database="pyqt5")

    def InsertData(self):
        connection = self.connection
        cursor = connection.cursor()
        sql = "INSERT INTO denemetable(name,email,phone) VALUES (%s,%s,%s)"
        values = (self.lineEdit1.text(),self.lineEdit2.text(),self.lineEdit3.text())
        cursor.execute(sql,values)
        connection.commit()
        QMessageBox.information(self,"Insert","Inserted was Successfully")
        self.close()

app = QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())