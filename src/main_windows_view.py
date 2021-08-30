# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_windows_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from consult_topics_view import Ui_Form

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1094, 731)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(18)
        sizePolicy.setVerticalStretch(18)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setStyleSheet("image:url(:/img/beach_image.png)\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.btn_consultar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_consultar.setGeometry(QtCore.QRect(490, 320, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_consultar.setFont(font)
        self.btn_consultar.setStyleSheet("QPushButton{\n"
"border-radius: 25px;\n"
"background-color: rgb(0, 21, 70);\n"
"color: rgb(255,255,255);\n"
"image: None;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(114, 159, 207);\n"
"\n"
"}")
        self.btn_consultar.setObjectName("btn_consultar")
        self.btn_salir = QtWidgets.QPushButton(self.centralwidget)
        self.btn_salir.setGeometry(QtCore.QRect(490, 400, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_salir.setFont(font)
        self.btn_salir.setStyleSheet("QPushButton{\n"
"border-radius: 25px;\n"
"background-color: rgb(0, 21, 70);\n"
"color: rgb(255,255,255);\n"
"image:None;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(114, 159, 207);\n"
"\n"
"}")
        self.btn_salir.setObjectName("btn_salir")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 250, 491, 51))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"color: rgb(0, 21, 70);\n"
"image: None;\n"
"\n"
"}")
        self.label_2.setObjectName("label_2")
        self.btn_salir.raise_()
        self.btn_consultar.raise_()
        self.label_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

#self.btn_salir.clicked(lambda: self.close_win(MainWindow))
        self.btn_consultar.clicked.connect(self.connect_to_consult_topics)
        self.btn_salir.clicked.connect(self.close_win)

    def close_win(self, MainWindow):
            sys.exit()

    def connect_to_consult_topics(self):
            self.Form = QtWidgets.QWidget()
            self.ui = Ui_Form()
            self.ui.setupUi(self.Form) 
            self.Form.show()



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Inicio"))
        self.btn_consultar.setText(_translate("MainWindow", "Consultar"))
        self.btn_salir.setText(_translate("MainWindow", "Salir"))
        self.label_2.setText(_translate("MainWindow", "¿Mejores lugares para hacer turismo en RD?"))

import image_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

