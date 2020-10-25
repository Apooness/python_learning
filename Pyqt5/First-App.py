import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setWindowTitle("İlk Uygulamam")
        self.resize(700,700)
        self.setWindowIcon(QIcon("indir.png"))
        self.setToolTip("First App")
        self.initUI()

    def initUI(self):
        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setText("Adınız: ")
        self.lbl_name.move(50,30)

        self.lbl_surname = QtWidgets.QLabel(self)
        self.lbl_surname.setText("Soyadınız: ")
        self.lbl_surname.move(50,60)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.move(110,130)

        self.txt_name = QtWidgets.QLineEdit(self)
        self.txt_name.resize(150,30)
        self.txt_name.move(110,30)
        
        self.txt_surname = QtWidgets.QLineEdit(self)
        self.txt_surname.resize(150,30)
        self.txt_surname.move(110,60)

        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.move(110,90)
        self.btn_save.setText("Kaydet")
        self.btn_save.clicked.connect(self.clicked)

    def clicked(self):
        self.lbl_result.setText(f"Ad: {self.txt_name.text()}\nSoyad: {self.txt_surname.text()}")


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()