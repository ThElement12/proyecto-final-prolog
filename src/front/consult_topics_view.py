# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'consult_topics_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1085, 488)
        self.btn_consultar = QtWidgets.QPushButton(Form)
        self.btn_consultar.setGeometry(QtCore.QRect(430, 80, 211, 51))
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
        self.btn_consultar_2 = QtWidgets.QPushButton(Form)
        self.btn_consultar_2.setGeometry(QtCore.QRect(120, 80, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_consultar_2.setFont(font)
        self.btn_consultar_2.setStyleSheet("QPushButton{\n"
"border-radius: 25px;\n"
"background-color: rgb(0, 21, 70);\n"
"color: rgb(255,255,255);\n"
"\n"
"}")
        self.btn_consultar_2.setObjectName("btn_consultar_2")
        self.btn_consultar_3 = QtWidgets.QPushButton(Form)
        self.btn_consultar_3.setGeometry(QtCore.QRect(430, 230, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_consultar_3.setFont(font)
        self.btn_consultar_3.setStyleSheet("QPushButton{\n"
"border-radius: 25px;\n"
"background-color: rgb(0, 21, 70);\n"
"color: rgb(255,255,255);\n"
"\n"
"}")
        self.btn_consultar_3.setObjectName("btn_consultar_3")
        self.btn_consultar_4 = QtWidgets.QPushButton(Form)
        self.btn_consultar_4.setGeometry(QtCore.QRect(750, 80, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_consultar_4.setFont(font)
        self.btn_consultar_4.setStyleSheet("QPushButton{\n"
"border-radius: 25px;\n"
"background-color: rgb(0, 21, 70);\n"
"color: rgb(255,255,255);\n"
"\n"
"}")
        self.btn_consultar_4.setObjectName("btn_consultar_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_consultar.setText(_translate("Form", "Restaurantes"))
        self.btn_consultar_2.setText(_translate("Form", "Hoteles"))
        self.btn_consultar_3.setText(_translate("Form", "Terrazas"))
        self.btn_consultar_4.setText(_translate("Form", "Playas"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

