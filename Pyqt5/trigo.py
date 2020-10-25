import sys
from PyQt5 import QtWidgets
from trigodesign import Ui_MainWindow
from math import sin,cos,tan,radians


class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnSec.clicked.connect(self.Hesapla)

    def Hesapla(self):
        chooses = self.ui.groupTri.findChildren(QtWidgets.QRadioButton)
        for choose in chooses:
            if choose.isChecked():
                if choose.text() == "Sinüs":
                    degree = int(self.ui.txtAci.text())
                    radian = radians(degree)
                    self.ui.lblSonuc.setText(str(sin(radian)))

                elif choose.text() == "Cosinüs":
                    degree = int(self.ui.txtAci.text())
                    radian = radians(degree)
                    self.ui.lblSonuc.setText(str(cos(radian)))

                elif choose.text() == "Tanjant":
                    degree = int(self.ui.txtAci.text())
                    radian = radians(degree)
                    self.ui.lblSonuc.setText(str(tan(radian)))

                else:
                    degree = int(self.ui.txtAci.text())
                    radian = radians(degree)
                    self.ui.lblSonuc.setText(str(1/(tan(radian))))

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())
app()
