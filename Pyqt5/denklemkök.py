from PyQt5 import QtWidgets
import sys
from DenklemKökdesign import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnBul.clicked.connect(self.KokBul)

    def KokBul(self):
        a = int(self.ui.txta.text())
        b = int(self.ui.txtb.text())
        c = int(self.ui.txtc.text())
        disk = (b**2) - (4*a*c)
        kok1 = (((-1*b) - (disk**0.5)) / (2*a))
        kok2 = (((-1*b) + (disk**0.5)) / (2*a))

        if b > 0:
            if c > 0:
                denklem = f"{a}x²+{b}x+{c}"
                self.ui.lblDenklem.setText(denklem)
            elif c == 0:
                denklem = f"{a}x²+{b}x"
                self.ui.lblDenklem.setText(denklem)
            else:
                denklem = f"{a}x²+{b}x{c}"
                self.ui.lblDenklem.setText(denklem)

        elif b == 0:
            if c > 0:
                denklem = f"{a}x²+{c}"
                self.ui.lblDenklem.setText(denklem)
            elif c == 0:
                denklem = f"{a}x²"
                self.ui.lblDenklem.setText(denklem)
            else:
                denklem = f"{a}x²{c}"
                self.ui.lblDenklem.setText(denklem)
        
        else:
            if c>0:
                denklem = f"{a}x²{b}x+{c}"
                self.ui.lblDenklem.setText(denklem)
            elif c == 0:
                denklem = f"{a}x²{b}x"
                self.ui.lblDenklem.setText(denklem)
            else:
                denklem = f"{a}x²{b}x{c}"
                self.ui.lblDenklem.setText(denklem)

        self.ui.lblKok1.setText("1. Kök:\t"+str(kok1))
        self.ui.lblKok2.setText("2. Kök:\t"+str(kok2))        




def window():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())
window()
