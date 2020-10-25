from PyQt5 import QtWidgets
import sys
from kmhtompsdesign import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnkmhtomps.clicked.connect(self.kmhtomps)
        self.ui.btnmpstokmh.clicked.connect(self.mpstokmh)

    def kmhtomps(self):
        kmh = int(self.ui.txtKmh.text())
        mps = (kmh*10)/36
        self.ui.lblMps.setText(str(mps))

    def mpstokmh(self):
        mps = int(self.ui.txtMps.text())
        kmh = mps * 3.6
        self.ui.lblKmh.setText(str(kmh))


def window():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())
window()
