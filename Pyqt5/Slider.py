import sys
from PyQt5 import QtWidgets
from sliderdesign import Ui_MainWindow
from PyQt5.QtGui import QPixmap


class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.hSlider.valueChanged[int].connect(self.ValueSlider)
        self.ui.lineEdit.textChanged.connect(self.ValueEdit)
        self.ui.lblSes.setPixmap(QPixmap("Sound/NoSound.png"))
        self.ui.lineEdit.setText("0")

    def ValueSlider(self, value):
        size = str(self.ui.hSlider.value())
        self.ui.lineEdit.setText(str(size))
        
        if value == 0:
            self.ui.lblSes.setPixmap(QPixmap("Sound/NoSound.png"))
        elif 0<value<=33:
            self.ui.lblSes.setPixmap(QPixmap("Sound/0-33.png"))
        elif 33<value<=66:
            self.ui.lblSes.setPixmap(QPixmap("Sound/34-66.png"))
        else:
            self.ui.lblSes.setPixmap(QPixmap("Sound/67-100.png"))

    def ValueEdit(self,value):
        linesize = self.ui.lineEdit.text()
        self.ui.hSlider.setValue(int(linesize))
        value = int(value)

        if value == 0:
            self.ui.lblSes.setPixmap(QPixmap("Sound/NoSound.png"))
        elif 0<value<=33:
            self.ui.lblSes.setPixmap(QPixmap("Sound/0-33.png"))
        elif 33<value<=66:
            self.ui.lblSes.setPixmap(QPixmap("Sound/34-66.png"))
        else:
            self.ui.lblSes.setPixmap(QPixmap("Sound/67-100.png"))


def App():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())
App()