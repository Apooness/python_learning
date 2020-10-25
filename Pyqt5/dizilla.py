from PyQt5 import QtWidgets
import sys
from dizilladesign import Ui_MainWindow
from PyQt5.QtWidgets import QTableWidgetItem
import requests
from bs4 import BeautifulSoup


class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tableDiziler.setHorizontalHeaderLabels(("AD","KATEGORİ"))
        self.ui.tableDiziler.setColumnWidth(0,200)
        self.ui.tableDiziler.setColumnWidth(1,400)
        self.ui.btnTop100.clicked.connect(self.Top100)
        self.ui.btnEniyi.clicked.connect(self.Besties)

    def Besties(self):
        rowtitleindex = 0
        rowcategoryindex = 0
        titleList = []
        categoryList = []
        url = "https://dizilla.com/trend/"
        html = requests.get(url).content
        soup = BeautifulSoup(html,"html.parser")
        liste = soup.find("tbody").findAll("tr")
        for i in liste:
            title = i.find("td",{"class":""}).find("span").text.strip()
            category = i.find("td",{"class":"text-white text-xxsmall"}).text.strip()
            titleList.append(title)
            categoryList.append(category)

        for title in titleList:
            self.ui.tableDiziler.setRowCount(len(titleList))
            self.ui.tableDiziler.setItem(rowtitleindex,0,QTableWidgetItem(title))
            rowtitleindex += 1
        for category in categoryList:
            self.ui.tableDiziler.setItem(rowcategoryindex,1,QTableWidgetItem(category))
            rowcategoryindex += 1

    def Top100(self):
        rowtitleindex = 0
        rowcategoryindex = 0
        titleList = []
        categoryList = []
        url = "https://dizilla.com/imdb-top-100/"
        html = requests.get(url).content
        soup = BeautifulSoup(html,"html.parser")
        liste = soup.find("tbody").findAll("tr")

        for i in liste:
            titles = i.find("a").find("span").text.strip()
            categories = i.find("td",{"class":"text-white text-xxsmall"}).text.strip()
            titleList.append(titles)
            categoryList.append(categories)

        for title in titleList:
            self.ui.tableDiziler.setRowCount(len(titleList))
            self.ui.tableDiziler.setItem(rowtitleindex,0,QTableWidgetItem(title))
            rowtitleindex += 1
        for category in categoryList:
            self.ui.tableDiziler.setItem(rowcategoryindex,1,QTableWidgetItem(category))
            rowcategoryindex += 1



def window():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())
window()
