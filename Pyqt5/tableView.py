import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from tableViewdesign import Ui_MainWindow


class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.loadProducts()
        self.ui.btnSave.clicked.connect(self.ProductSave)

    def ProductSave(self):
        name = self.ui.txtName.text()
        price = self.ui.txtPrice.text()

        if name and price is not None:
            rowcount = self.ui.tableProducts.rowCount()
            self.ui.tableProducts.insertRow(rowcount)
            self.ui.tableProducts.setItem(rowcount,1,QTableWidgetItem(price))
            self.ui.tableProducts.setItem(rowcount,0,QTableWidgetItem(name))

    def loadProducts(self):
        products = [
            {"name":"Huawei P30","price":3000},
            {"name":"Huawei Mate30","price":4000},
            {"name":"Huawei P40","price":5000},
            {"name":"Huawei Mate40","price":6000}
        ]

        self.ui.tableProducts.setRowCount(len(products))
        self.ui.tableProducts.setColumnCount(2)
        self.ui.tableProducts.setHorizontalHeaderLabels(("Name","Price"))
        self.ui.tableProducts.setColumnWidth(1,100)
        self.ui.tableProducts.setColumnWidth(0,200)

        rowindex = 0
        for product in products:
            self.ui.tableProducts.setItem(rowindex,0,QTableWidgetItem(product["name"]))
            self.ui.tableProducts.setItem(rowindex,1,QTableWidgetItem(str(product["price"])))
            rowindex+=1

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())
app()
