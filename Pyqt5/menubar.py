import sys
from PyQt5 import QtWidgets, QtGui
from menubardesign import Ui_MainWindow
from PyQt5.QtWidgets import QMessageBox, QMenu, QAction
from PyQt5.QtGui import QIcon

class myApp(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(myApp,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionNew.triggered.connect(self.NewFile)
        self.ui.actionOpen.triggered.connect(self.OpenFile)
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionSave.triggered.connect(self.SaveFile)
        self.ui.actionDelete.triggered.connect(self.DeleteFile)
        self.ui.actionHelp.triggered.connect(self.Help)
        self.ui.actionTools_Tab.triggered.connect(self.ToolsTab)
        self.ui.actionStatus_Bar.triggered.connect(self.StatusBar)
        

    def SaveFile(self):
        self.ui.lblSonuc.setText("File was Saved")
    def NewFile(self):
        self.ui.lblSonuc.setText("New was pressed")
    def OpenFile(self):
        self.ui.lblSonuc.setText("Open was pressed")
    def DeleteFile(self):
        self.ui.lblSonuc.setText("File was Deleted")
    def Help(self):
        QMessageBox.information(self,"Info","This is Information for this app",QMessageBox.NoButton)  
  
    def StatusBar(self,state):
        if state:
            self.ui.statusbar.show()
        else:
            self.ui.statusbar.hide()

    def contextMenuEvent(self,event):
        contextMenu = QMenu(self)
        contextMenu.addActions([self.ui.actionNew,self.ui.actionExit])
        contextMenu.exec_(self.mapToGlobal(event.pos()))

    def ToolsTab(self,toolbar):
        if toolbar:
            self.ui.toolBar.show()
        else:
            self.ui.toolBar.hide()


def window():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())
window()