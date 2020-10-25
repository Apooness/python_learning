import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyCalculator(QMainWindow):
    def __init__(self):
        super(MyCalculator,self).__init__()
        self.setWindowTitle("Hesap Makinesi")
        self.resize(600,600)
        self.initUI()

    def initUI(self):
        self.lbl_sayi1 = QtWidgets.QLabel(self)
        self.lbl_sayi1.setText("1. sayı: ")
        self.lbl_sayi1.move(50,30)
        
        self.txt_sayi1 = QtWidgets.QLineEdit(self)
        self.txt_sayi1.move(100,30)

        self.lbl_sayi2 = QtWidgets.QLabel(self)
        self.lbl_sayi2.setText("2. sayı: ")
        self.lbl_sayi2.move(50,80)

        self.txt_sayi2 = QtWidgets.QLineEdit(self)
        self.txt_sayi2.move(100,80)

        self.btn_topla = QtWidgets.QPushButton(self)
        self.btn_topla.move(100,150)
        self.btn_topla.setText("Topla")
        self.btn_topla.clicked.connect(self.topla)

        self.btn_cikar = QtWidgets.QPushButton(self)
        self.btn_cikar.move(200,150)
        self.btn_cikar.setText("Çıkar")
        self.btn_cikar.clicked.connect(self.cikar)

        self.btn_carp = QtWidgets.QPushButton(self)
        self.btn_carp.move(300,150)
        self.btn_carp.setText("Çarp")
        self.btn_carp.clicked.connect(self.carp)

        self.btn_bol = QtWidgets.QPushButton(self)
        self.btn_bol.move(400,150)
        self.btn_bol.setText("Böl")
        self.btn_bol.clicked.connect(self.bol)

        self.lbl_sonuc = QtWidgets.QLabel(self)
        self.lbl_sonuc.setText("Sonuç: ")
        self.lbl_sonuc.move(100,200)
        self.lbl_sonuc.setStyleSheet("QLabel{font:30pt}")
        self.lbl_sonuc.resize(400,400)

    def topla(self):
        result = int(self.txt_sayi1.text()) + int(self.txt_sayi2.text())
        self.lbl_sonuc.setText(f"""Sonuç: {result}""")

    def cikar(self):
        result = int(self.txt_sayi1.text()) - int(self.txt_sayi2.text())
        self.lbl_sonuc.setText(f"Sonuç: {result}")

    def carp(self):
        result = int(self.txt_sayi1.text()) * int(self.txt_sayi2.text())
        self.lbl_sonuc.setText(f"Sonuç: {result}")

    def bol(self):
        result = int(self.txt_sayi1.text()) / int(self.txt_sayi2.text())
        self.lbl_sonuc.setText(f"Sonuç: {result}")
        
    

def window():
    app = QApplication(sys.argv)
    win = MyCalculator()
    win.show()
    sys.exit(app.exec_())

window()