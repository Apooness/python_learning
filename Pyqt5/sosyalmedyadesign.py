# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\sosyalmedyadesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(652, 193)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 40, 581, 51))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnInsta = QtWidgets.QPushButton(self.widget)
        self.btnInsta.setObjectName("btnInsta")
        self.horizontalLayout.addWidget(self.btnInsta)
        self.btnYt = QtWidgets.QPushButton(self.widget)
        self.btnYt.setObjectName("btnYt")
        self.horizontalLayout.addWidget(self.btnYt)
        self.btnGit = QtWidgets.QPushButton(self.widget)
        self.btnGit.setObjectName("btnGithub")
        self.horizontalLayout.addWidget(self.btnGit)
        self.btnTt = QtWidgets.QPushButton(self.widget)
        self.btnTt.setObjectName("btnTt")
        self.horizontalLayout.addWidget(self.btnTt)
        self.btnTc = QtWidgets.QPushButton(self.widget)
        self.btnTc.setObjectName("btnTc")
        self.horizontalLayout.addWidget(self.btnTc)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 652, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnInsta.setText(_translate("MainWindow", "Instagram"))
        self.btnYt.setText(_translate("MainWindow", "Youtube"))
        self.btnGit.setText(_translate("MainWindow", "Github"))
        self.btnTt.setText(_translate("MainWindow", "Twitter"))
        self.btnTc.setText(_translate("MainWindow", "Twitch"))
