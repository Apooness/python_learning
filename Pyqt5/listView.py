import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog,QLineEdit,QMessageBox
from listViewdesign import Ui_MainWindow
from menubar import myApp


class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.loadStudent()

        # Add Student
        self.ui.btnAdd.clicked.connect(self.addStudent)

        # Edit Student
        self.ui.btnEdit.clicked.connect(self.editStudent)

        # Remove Student
        self.ui.btnRemove.clicked.connect(self.removeStudent) 	

        # Up
        self.ui.btnUp.clicked.connect(self.upStudent)
        
        # Down
        self.ui.btnDown.clicked.connect(self.downStudent)

        # Sort
        self.ui.btnSort.clicked.connect(self.sortStudent)

        # Close
        self.ui.btnExit.clicked.connect(self.quit)

        

    def loadStudent(self):
        self.ui.listItems.addItems(["Berna","Ali","Mustafa","Sema"])
        self.ui.listItems.setCurrentRow(0)

    def addStudent(self):
        index = self.ui.listItems.currentRow()
        text , ok = QInputDialog.getText(self,"New Student","New Student's Name")
        if text and ok is not None:
            self.ui.listItems.insertItem(index,text)

    def editStudent(self):
        index = self.ui.listItems.currentRow()
        item = self.ui.listItems.item(index)
        if item is not None:
            text,ok = QInputDialog.getText(self,"Edit Student","Student Name",QLineEdit.Normal, item.text())
            if text and ok is not None:
                item.setText(text)

    def removeStudent(self):
        index = self.ui.listItems.currentRow()
        item = self.ui.listItems.item(index)
        if item is None:
            return
        
        q = QMessageBox.question(self,"Remove Student","Are You Sure?"+item.text(),QMessageBox.Yes|QMessageBox.No)
        if q == QMessageBox.Yes:
            item = self.ui.listItems.takeItem(index)
            del item

    def upStudent(self):
        index = self.ui.listItems.currentRow()
        if index >=1:
            item = self.ui.listItems.takeItem(index)
            self.ui.listItems.insertItem(index-1,item)
            self.ui.listItems.setCurrentItem(item)

    def downStudent(self):
        index = self.ui.listItems.currentRow()
        if index < self.ui.listItems.count()-1:
            item = self.ui.listItems.takeItem(index)
            self.ui.listItems.insertItem(index+1,item)
            self.ui.listItems.setCurrentItem(item)

        
    def sortStudent(self):
        self.ui.listItems.sortItems()

    def quit(self):
        quit()



def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())
app()
