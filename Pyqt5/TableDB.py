from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
from TableDBdesign import Ui_MainWindow
import mysql.connector

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnSave.clicked.connect(self.InsertDataDB)
        self.ui.btnNew.clicked.connect(self.NewRow)
        self.ConnectDB()
        self.show()
        QMessageBox.warning(self,"Info","Lütfen hepsini tek seferde giriniz!!!")

    def ConnectDB(self):
        self.connection = mysql.connector.connect(host="localhost",user="root",password="123456A789a",database="pyqt5")

    def InsertDataDB(self):
        row = 0
        while True:
            if row == self.ui.tableWidget.rowCount():
                break
            else:
                name = [self.ui.tableWidget.item(row,0).text()]
                email = [self.ui.tableWidget.item(row,1).text()]
                phone = [self.ui.tableWidget.item(row,2).text()]
                row +=1
                connection = self.connection
                cursor = connection.cursor()
                sql = "INSERT INTO denemetable(name,email,phone) VALUES(%s,%s,%s)"
                Values = ("".join(name),"".join(email),"".join(phone))
                cursor.execute(sql,Values)
                connection.commit()
        QMessageBox.information(self,"Insert","Inserted was successfully")

    def NewRow(self):
        row = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row)

def App():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())
App()
