# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(636, 619)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnDraw = QtWidgets.QPushButton(self.centralwidget)
        self.btnDraw.setGeometry(QtCore.QRect(180, 575, 70, 30))
        self.btnDraw.setObjectName("btnDraw")
        self.clientWidget = QtWidgets.QWidget(self.centralwidget)
        self.clientWidget.setGeometry(QtCore.QRect(10, 79, 621, 491))
        self.clientWidget.setObjectName("clientWidget")
        self.btnQuit = QtWidgets.QPushButton(self.centralwidget)
        self.btnQuit.setGeometry(QtCore.QRect(310, 575, 80, 30))
        self.btnQuit.setObjectName("btnQuit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnDraw.setText(_translate("MainWindow", "Draw"))
        self.btnQuit.setText(_translate("MainWindow", "Quit"))

