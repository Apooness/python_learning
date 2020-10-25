from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton, QWidget
import sys
import mysql.connector

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Connection DB")
        self.InitUI()

    def InitUI(self):
        self.button = QPushButton("Connect DB",self)
        self.button.resize(150,100)
        self.button.clicked.connect(self.ConnectDB)
        self.show()
   
    def ConnectDB(self):
        try:
            mysql.connector.connect(host="localhost",user="root",password="123456A789a")
            QMessageBox.information(self,"connection","Connection was successfully")
        except mysql.connector.Error as Err:
            QMessageBox.warning(self,"Connection",f"Connection was not successfully\nHata:{Err}")
            self.close()
def App():
    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())

App()
