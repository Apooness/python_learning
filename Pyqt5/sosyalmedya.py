from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
from sosyalmedyadesign import Ui_MainWindow
from selenium import webdriver
import time

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.driver = webdriver
        self.ui.btnInsta.clicked.connect(self.Instagram)
        self.ui.btnYt.clicked.connect(self.Youtube)
        self.ui.btnTc.clicked.connect(self.Twitch)
        self.ui.btnGit.clicked.connect(self.Github)
        self.ui.btnTt.clicked.connect(self.Twitter)


    def Instagram(self):
        answer = QMessageBox.question(self,"Are You follower?","Are You follow me in instagram?",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        if answer == QMessageBox.Yes:
            QMessageBox.information(self,"Thanks","Thank You for following me!!!",QMessageBox.Ok)
        else:
            answer = QMessageBox.question(self,"follow me?","Want to follow me?",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
            if answer == QMessageBox.Yes:
                answer = QMessageBox.question(self,"Links","Username: 'mustafaakilll'",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
                if answer == QMessageBox.Yes:
                    self.driver.Chrome().get("https://www.instagram.com/mustafaakilll/")
                    time.sleep(1)         

    def Youtube(self):
        answer = QMessageBox.question(self,"Are You follower?","Are You follow me in youtube?",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        if answer == QMessageBox.Yes:
            QMessageBox.information(self,"Thanks","Thank You for following me!!!",QMessageBox.Ok)
        else:
            answer = QMessageBox.question(self,"follow me?","Want to follow me?",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
            if answer == QMessageBox.Yes:
                answer = QMessageBox.question(self,"Links","Username: 'Selman Kahya'",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
                if answer == QMessageBox.Yes:
                    self.driver.Chrome().get("https://www.youtube.com/user/SirChintzy")
                    time.sleep(1)         

    def Twitch(self):
        answer = QMessageBox.question(self,"Are You follower?","Are You follow me in twitch?",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        if answer == QMessageBox.Yes:
            QMessageBox.information(self,"Thanks","Thank You for following me!!!",QMessageBox.Ok)
        else:
            answer = QMessageBox.question(self,"follow me?","Want to follow me?",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
            if answer == QMessageBox.Yes:
                answer = QMessageBox.question(self,"Links","Username: 'WhiteRose09'",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
                if answer == QMessageBox.Yes:
                    self.driver.Chrome().get("https://www.twitch.tv/whiterose09")
                    time.sleep(1)

    def Github(self):
        answer = QMessageBox.question(self,"Are You follower?","Are You follow me in Github?",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        if answer == QMessageBox.Yes:
            QMessageBox.information(self,"Thanks","Thank You for following me!!!",QMessageBox.Ok)
        else:
            answer = QMessageBox.question(self,"follow me?","Want to follow me?",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
            if answer == QMessageBox.Yes:
                answer = QMessageBox.question(self,"Links","Username: 'Apooness'",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
                if answer == QMessageBox.Yes:
                    self.driver.Chrome().get("https://github.com/Apooness")
                    time.sleep(1)

    def Twitter(self):
        answer = QMessageBox.question(self,"Are You follower?","Are You follow me in Twitter?",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        if answer == QMessageBox.Yes:
            QMessageBox.information(self,"Thanks","Thank You for following me!!!",QMessageBox.Ok)
        else:
            answer = QMessageBox.question(self,"follow me?","Want to follow me?",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
            if answer == QMessageBox.Yes:
                answer = QMessageBox.question(self,"Links","Username: 'mustafaakill'",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
                if answer == QMessageBox.Yes:
                    self.driver.Chrome().get("https://twitter.com/Mustafaakill")
                    time.sleep(1)


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())
app()