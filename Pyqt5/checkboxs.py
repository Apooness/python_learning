import sys
from PyQt5 import QtWidgets
from checkboxdesign import Ui_MainWindow
from PyQt5.QtWidgets import QMessageBox

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnOnayLesson.clicked.connect(self.GetLessons)
        self.ui.btnOnaySpor.clicked.connect(self.GetSpors)
        self.ui.btnquit.clicked.connect(self.CloseApp)

    def CloseApp(self):
        result = QMessageBox.question(self,"Applied???","Did you apply Lessons?",QMessageBox.Yes|QMessageBox.No)
        if result == QMessageBox.Yes:
            result2 = QMessageBox.question(self,"Applied???","Did you apply Spors?",QMessageBox.Yes|QMessageBox.No)
            if result2 == QMessageBox.Yes:
                QMessageBox.question(self,"Thanks","Thanks for choices",QMessageBox.Ok)
                QtWidgets.qApp.quit()
            else:
                QMessageBox.question(self,"Go Back","Choose Spors",QMessageBox.Ok)
        else:
            QMessageBox.question(self,"Go Back","Apply Lessons",QMessageBox.Ok)

    def GetSpors(self):
        sporresult = ""
        spors = self.ui.groupSpors.findChildren(QtWidgets.QCheckBox)
        for spor in spors:
            if spor.isChecked():
                sporresult += spor.text() + "\n"
        self.ui.lblspors.setText(sporresult)

    def GetLessons(self):
        dersresult = ""
        derss = self.ui.groupDerss.findChildren(QtWidgets.QCheckBox)
        for ders in derss:
            if ders.isChecked():
                dersresult += ders.text() + "\n"
        self.ui.lblders.setText(dersresult)
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()
