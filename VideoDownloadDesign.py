# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VideoDownloadDesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setIconSize(QtCore.QSize(100, 100))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 150, 391, 61))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.indirtext = QtWidgets.QLineEdit(self.centralwidget)
        self.indirtext.setGeometry(QtCore.QRect(10, 240, 781, 31))
        self.indirtext.setObjectName("indirtext")
        self.indirbutton = QtWidgets.QPushButton(self.centralwidget)
        self.indirbutton.setGeometry(QtCore.QRect(350, 290, 51, 41))
        self.indirbutton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/enes_/OneDrive/Masaüstü/PythonEgitimleri/YoutubeVideoIndirFormUygulaması/button-ıcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.indirbutton.setIcon(icon)
        self.indirbutton.setIconSize(QtCore.QSize(150, 150))
        self.indirbutton.setObjectName("indirbutton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.label.setText(_translate("MainWindow", "İndirmek İstediğiniz Linki Yapıştırın"))
