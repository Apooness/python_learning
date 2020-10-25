from PyQt5 import QtWidgets
import sys
from SpeedTestdesign import Ui_MainWindow
from speedtest import Speedtest


class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnDownload.clicked.connect(self.DownloadSpeed)
        self.ui.btnUpload.clicked.connect(self.UploadSpeed)

    def DownloadSpeed(self):
        self.ui.lblDownload.setText(str(round(Speedtest().download() / 1_000_000 , 2)))

    def UploadSpeed(self):
        self.ui.lblUpload.setText(str(round(Speedtest().upload() / 1_000_000 , 2)))

def window():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())
window()
