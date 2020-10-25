from PyQt5 import QtWidgets
import sys
from imdbListedesign import Ui_MainWindow
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtGui import QIcon
import requests
from bs4 import BeautifulSoup

class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("imgs/indir.png"))        
        self.ui.tableListe.setHorizontalHeaderLabels(("AD","YIL","RATİNG"))
        self.ui.tableListe.setColumnWidth(0,380)
        self.ui.tableListe.setColumnWidth(1,100)
        self.ui.tableListe.setColumnWidth(2,100)
        self.LoadOptions()
        self.ui.btnOnayla.clicked.connect(self.ShowTable)

    def LoadOptions(self):
        liste = ["Top Diziler","Top Filmler","Trend Diziler","Trend Filmler"]
        self.ui.cbSecenek.addItems(liste)
    
    def GetInfo(self,url):
        url = url
        html = requests.get(url).content
        soup = BeautifulSoup(html,"html.parser")
        liste = soup.find("tbody",{"class":"lister-list"}).findAll("tr",)
        return liste

    def InserttoTable(self,liste):
        rowtitleindex = 0
        rowyearindex = 0
        rowratingindex = 0 
        titleList = []
        yearList = []
        ratingList = []        
        for i in liste:
            title = i.find("td",{"class":"titleColumn"}).find("a").text
            year = i.find("td",{"class":"titleColumn"}).find("span").text.strip("()")
            rating = i.find("td",{"class":"ratingColumn imdbRating"}).text.strip()
            titleList.append(title)
            yearList.append(year)
            ratingList.append(rating)
        for title in titleList:
            self.ui.tableListe.setRowCount(len(titleList))
            self.ui.tableListe.setItem(rowtitleindex,0,QTableWidgetItem(title))
            rowtitleindex += 1
        for year in yearList:
            self.ui.tableListe.setItem(rowyearindex,1,QTableWidgetItem(year))
            rowyearindex += 1
        for rating in ratingList:
            self.ui.tableListe.setItem(rowratingindex,2,QTableWidgetItem(rating))
            rowratingindex += 1


    def ShowTable(self):
        secim = self.ui.cbSecenek.currentText()
        if secim == "Top Diziler":
            liste = self.GetInfo("https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250")
            self.InserttoTable(liste)

        elif secim == "Trend Diziler":
            liste = self.GetInfo("https://www.imdb.com/chart/tvmeter/?ref_=nv_tvv_mptv")
            self.InserttoTable(liste)

        elif secim == "Top Filmler":
            liste = self.GetInfo("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
            self.InserttoTable(liste)

        else:
            liste = self.GetInfo("https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm")
            self.InserttoTable(liste)
                

def window():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())
window()
