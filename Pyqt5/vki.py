from PyQt5 import QtWidgets
import sys
from vkidesign import Ui_MainWindow
# kilo/boy**2
class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnHesapla.clicked.connect(self.Hesapla)

    def Hesapla(self):
        # boy = self.ui.txtBoy.text()
        # boy = float(boy)/100
        # kilo = self.ui.txtKilo.text()
        # kilo = float(kilo)
        # sonuc = kilo/(boy**2)
        # self.ui.lblSonuc.setText("Kütle İndeksiniz: "+str(sonuc))
        self.ui.lblSonuc.setText("Kütle İndeksiniz: "+str(float(self.ui.txtKilo.text())/((float(self.ui.txtBoy.text())/100)**2)))

def window():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())
window()
