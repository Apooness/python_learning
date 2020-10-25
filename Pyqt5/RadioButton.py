import sys
from PyQt5 import QtWidgets
from RadioButtondesign import Ui_MainWindow


class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.rbTurkiye.setChecked(True)
        self.ui.rbLise.setChecked(True)
        self.ui.btnEgitim.clicked.connect(self.SelectedEducation)
        self.ui.btnUlke.clicked.connect(self.selectedCountry)
        self.ui.btnSehir.clicked.connect(self.SelectedCity)
        self.ui.btnSeviye.clicked.connect(self.SelectedLevel)

    def SelectedLevel(self):
        level = self.ui.cbSeviye.currentText()
        self.ui.lblSeviye.setText("Seçilen Seviye: "+level)

    def SelectedCity(self):
        city = self.ui.cbSehirler.currentText()
        self.ui.lblSehir.setText("Seçilen Şehir: "+city)

    def selectedCountry(self):
        Countries = self.ui.groupUlke.findChildren(QtWidgets.QRadioButton)
        for Country in Countries:
            if Country.isChecked():
                self.ui.lblUlke.setText("Seçilen Ülke: "+Country.text())
                if Country.text() == "Türkiye":
                    sehirlerTurkey = ["Ankara","Istanbul","Izmir"]
                    self.ui.cbSehirler.addItems(sehirlerTurkey)
                elif Country.text() == "Almanya":
                    sehirlerGermany = ["Berlin","Munich","Köln"]
                    self.ui.cbSehirler.addItems(sehirlerGermany)
                elif Country.text() == "İngiltere":
                    sehirlerEngland = ["London","Liverpool","Manchester"]
                    self.ui.cbSehirler.addItems(sehirlerEngland)
                else:
                    sehirlerAmerica = ["Chicago","Washington","New York"]
                    self.ui.cbSehirler.addItems(sehirlerAmerica)
                
    def SelectedEducation(self):
        Educations = self.ui.groupEgitim.findChildren(QtWidgets.QRadioButton)
        for Education in Educations:
            if Education.isChecked():
                self.ui.lblEgitim.setText("Seçilen Ülke: "+Education.text())
                if Education.text() == "Lise":
                    list = ["Fen Lisesi","Meslek Lisesi","Anadolu Lisesi"]
                    self.ui.cbSeviye.addItems(list)
                elif Education.text() == "Üniversite":
                    list = ["Lisans","Önlisans","Yüksek Lisans"]
                    self.ui.cbSeviye.addItesm(list)
                else:
                    continue

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()