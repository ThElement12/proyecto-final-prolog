# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_windows.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from consult_topics import Ui_Form
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1086, 716)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 250, 491, 51))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"color: rgb(0, 21, 70);\n"
"\n"
"}")
        self.label_2.setObjectName("label_2")
        self.btn_consultar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_consultar.setGeometry(QtCore.QRect(520, 340, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_consultar.setFont(font)
        self.btn_consultar.setStyleSheet("QPushButton{\n"
"border-radius: 25px;\n"
"background-color: rgb(0, 21, 70);\n"
"color: rgb(255,255,255);\n"
"\n"
"}")
        self.btn_consultar.setObjectName("btn_consultar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-320, -110, 1501, 991))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../resources/beach_image.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.btn_salir = QtWidgets.QPushButton(self.centralwidget)
        self.btn_salir.setGeometry(QtCore.QRect(520, 420, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_salir.setFont(font)
        self.btn_salir.setStyleSheet("QPushButton{\n"
"border-radius: 25px;\n"
"background-color: rgb(0, 21, 70);\n"
"color: rgb(255,255,255);\n"
"\n"
"}")
        self.btn_salir.setObjectName("btn_salir")
        self.label.raise_()
        self.btn_consultar.raise_()
        self.label_2.raise_()
        self.btn_salir.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btn_consultar.clicked.connect(self.click)
        self.btn_salir.clicked.connect(lambda:self.closescr(MainWindow))
    def click(self):
        #code the 2nd screen here
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        self.Form.show()

    def closescr(self,MainWindow):
        #hide the screen on exit btn clicked
        sys.exit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "¿Mejores lugares para hacer turismo en RD?"))
        self.btn_consultar.setText(_translate("MainWindow", "Consultar"))
        self.btn_salir.setText(_translate("MainWindow", "Salir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

