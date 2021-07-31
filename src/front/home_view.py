# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1081, 717)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-350, -110, 1501, 991))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../resources/beach_image.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.btn_consultar = QtWidgets.QPushButton(Form)
        self.btn_consultar.setGeometry(QtCore.QRect(460, 360, 211, 51))
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
        self.btn_salir = QtWidgets.QPushButton(Form)
        self.btn_salir.setGeometry(QtCore.QRect(460, 440, 211, 51))
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
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(310, 270, 491, 51))
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_consultar.setText(_translate("Form", "Consultar"))
        self.btn_salir.setText(_translate("Form", "Salir"))
        self.label_2.setText(_translate("Form", "¿Mejores lugares para hacer turismo en RD?"))

import image_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

