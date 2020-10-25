import sys
from PyQt5 import QtWidgets
from photodesign import Ui_MainWindow
from PyQt5.QtGui import QPixmap

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnCat.clicked.connect(self.ShowCat)
        self.ui.btnDog.clicked.connect(self.ShowDog)

    def ShowCat(self):
        self.ui.lblphoto.setPixmap(QPixmap("imgs/cat.jpg"))

    def ShowDog(self):
        self.ui.lblphoto.setPixmap(QPixmap("imgs/dog.jpg"))



def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())
app()
