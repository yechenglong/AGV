# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '小车.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.xiaoche = QtWidgets.QLabel(self.centralwidget)
        self.xiaoche.setGeometry(QtCore.QRect(130, 80, 54, 12))
        self.xiaoche.setObjectName("xiaoche")
        self.xiaoche_name = QtWidgets.QTextEdit(self.centralwidget)
        self.xiaoche_name.setGeometry(QtCore.QRect(160, 50, 104, 71))
        self.xiaoche_name.setObjectName("xiaoche_name")
        self.jiedian = QtWidgets.QLabel(self.centralwidget)
        self.jiedian.setGeometry(QtCore.QRect(30, 230, 54, 12))
        self.jiedian.setObjectName("jiedian")
        self.jiedian_name = QtWidgets.QTextEdit(self.centralwidget)
        self.jiedian_name.setGeometry(QtCore.QRect(60, 200, 104, 71))
        self.jiedian_name.setObjectName("jiedian_name")
        self.daoda = QtWidgets.QPushButton(self.centralwidget)
        self.daoda.setGeometry(QtCore.QRect(180, 230, 75, 23))
        self.daoda.setObjectName("daoda")
        self.shangliao = QtWidgets.QPushButton(self.centralwidget)
        self.shangliao.setGeometry(QtCore.QRect(300, 230, 75, 23))
        self.shangliao.setObjectName("shangliao")
        self.xiaoliao = QtWidgets.QPushButton(self.centralwidget)
        self.xiaoliao.setGeometry(QtCore.QRect(430, 230, 75, 23))
        self.xiaoliao.setObjectName("xiaoliao")
        self.tingche = QtWidgets.QPushButton(self.centralwidget)
        self.tingche.setGeometry(QtCore.QRect(540, 230, 75, 23))
        self.tingche.setObjectName("tingche")
        self.ip = QtWidgets.QLabel(self.centralwidget)
        self.ip.setGeometry(QtCore.QRect(300, 50, 54, 12))
        self.ip.setObjectName("ip")
        self.port = QtWidgets.QLabel(self.centralwidget)
        self.port.setGeometry(QtCore.QRect(300, 110, 71, 16))
        self.port.setObjectName("port")
        self.ip_input = QtWidgets.QTextEdit(self.centralwidget)
        self.ip_input.setGeometry(QtCore.QRect(380, 40, 221, 41))
        self.ip_input.setObjectName("ip_input")
        self.port_input = QtWidgets.QTextEdit(self.centralwidget)
        self.port_input.setGeometry(QtCore.QRect(380, 100, 221, 41))
        self.port_input.setObjectName("port_input")
        self.lianjie = QtWidgets.QPushButton(self.centralwidget)
        self.lianjie.setGeometry(QtCore.QRect(650, 70, 75, 23))
        self.lianjie.setObjectName("lianjie")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 410, 81, 16))
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(90, 380, 621, 161))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 619, 159))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 611, 141))
        self.textBrowser.setObjectName("textBrowser")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
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
        self.xiaoche.setText(_translate("MainWindow", "小车"))
        self.jiedian.setText(_translate("MainWindow", "节点"))
        self.daoda.setText(_translate("MainWindow", "到达"))
        self.shangliao.setText(_translate("MainWindow", "上料完成"))
        self.xiaoliao.setText(_translate("MainWindow", "下料完成"))
        self.tingche.setText(_translate("MainWindow", "停车完成"))
        self.ip.setText(_translate("MainWindow", "服务器ip"))
        self.port.setText(_translate("MainWindow", "服务器port"))
        self.lianjie.setText(_translate("MainWindow", "连接"))
        self.label.setText(_translate("MainWindow", "收到的消息"))

