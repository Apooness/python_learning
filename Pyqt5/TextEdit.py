import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QFontDialog, QMainWindow, QPushButton, QTextEdit, QLabel, QColorDialog, QFileDialog

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Deneme")
        self.setGeometry(100,100,500,500)
        self.InitUi()

    def InitUi(self):

        self.buttonOpen = QPushButton("Open File!!!",self)
        self.buttonOpen.move(100,40)
        self.buttonOpen.clicked.connect(self.OpenFile)

        self.buttonSave = QPushButton("Save File!!!",self)
        self.buttonSave.move(200,40)
        self.buttonSave.clicked.connect(self.SaveFile)

        self.buttonFont = QPushButton("Font!!!",self)
        self.buttonFont.move(200,70)
        self.buttonFont.clicked.connect(self.FontText)

        self.buttonColor = QPushButton("Color!!!",self)
        self.buttonColor.move(100,70)
        self.buttonColor.clicked.connect(self.ColorText)

        self.TextEdit = QTextEdit(self)
        self.TextEdit.setGeometry(100,100,300,200)
        self.show()

    def SaveFile(self):
        QFileDialog.getSaveFileName(self,"Save File")

    def OpenFile(self):
        filename = QFileDialog.getOpenFileName(self,"Open File")
        with open (filename[0],"r",encoding="UTF-8") as file:
            data = file.read()
            self.TextEdit.setText(data)
        



    def FontText(self):
        font,ok = QFontDialog.getFont()
        
        if ok:
            self.TextEdit.setFont(font)

    def ColorText(self):
        color = QColorDialog.getColor()
        self.TextEdit.setTextColor(color)        



app = QApplication(sys.argv)
win = App()
sys.exit(app.exec())
