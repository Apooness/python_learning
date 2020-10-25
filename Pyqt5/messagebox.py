from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from messageboxdesign import Ui_MainWindow
import sys

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnQuit.clicked.connect(self.showDialog)

    def showDialog(self):
        result = QMessageBox.question(self,"Close App","Are You Sure???",QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore)
        if result == QMessageBox.Ok:
            result2 = QMessageBox.question(self,"Sure???","Are You Sure??? Again",QMessageBox.Ok | QMessageBox.Cancel)
            if result2 == QMessageBox.Ok:
                msg = QMessageBox()
                msg.setText("You free to go!!!")
                msg.setWindowTitle("Good Bye")
                msg.exec_()
                QtWidgets.qApp.quit()


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()