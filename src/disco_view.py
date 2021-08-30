# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'disco_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1093, 500)
        Dialog.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(247, 209, 209, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_place_icon = QtWidgets.QPushButton(Dialog)
        self.pushButton_place_icon.setGeometry(QtCore.QRect(70, 80, 71, 41))
        self.pushButton_place_icon.setStyleSheet("QPushButton{\n"
"border-radius: 20px;\n"
"background-color: transparent;\n"
"color: rgb(0,0,0);\n"
"font-family: Century SchoolBook L;\n"
"font-weight: bold;\n"
"\n"
"}")
        self.pushButton_place_icon.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resources/place_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_place_icon.setIcon(icon)
        self.pushButton_place_icon.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_place_icon.setObjectName("pushButton_place_icon")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(60, 170, 91, 51))
        self.pushButton.setStyleSheet("QPushButton{\n"
"border-radius: 20px;\n"
"background-color: transparent;\n"
"color: rgb(0,0,0);\n"
"font-family: Century SchoolBook L;\n"
"font-weight: bold;\n"
"\n"
"}")
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../resources/budget_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_place_icon_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_place_icon_2.setGeometry(QtCore.QRect(70, 250, 71, 51))
        self.pushButton_place_icon_2.setStyleSheet("QPushButton{\n"
"border-radius: 20px;\n"
"background-color: transparent;\n"
"color: rgb(0,0,0);\n"
"font-family: Century SchoolBook L;\n"
"font-weight: bold;\n"
"\n"
"}")
        self.pushButton_place_icon_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../resources/scores_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_place_icon_2.setIcon(icon2)
        self.pushButton_place_icon_2.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_place_icon_2.setObjectName("pushButton_place_icon_2")
        self.pushButton_place_icon_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_place_icon_3.setGeometry(QtCore.QRect(70, 330, 71, 51))
        self.pushButton_place_icon_3.setStyleSheet("QPushButton{\n"
"border-radius: 20px;\n"
"background-color: transparent;\n"
"color: rgb(0,0,0);\n"
"font-family: Century SchoolBook L;\n"
"font-weight: bold;\n"
"\n"
"}")
        self.pushButton_place_icon_3.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../resources/economy_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_place_icon_3.setIcon(icon3)
        self.pushButton_place_icon_3.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_place_icon_3.setObjectName("pushButton_place_icon_3")
        self.label_disco_recommended = QtWidgets.QLabel(Dialog)
        self.label_disco_recommended.setGeometry(QtCore.QRect(470, 80, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setBold(True)
        font.setWeight(75)
        self.label_disco_recommended.setFont(font)
        self.label_disco_recommended.setStyleSheet("background-color: transparent;")
        self.label_disco_recommended.setObjectName("label_disco_recommended")
        self.pushButton_consult_disco = QtWidgets.QPushButton(Dialog)
        self.pushButton_consult_disco.setGeometry(QtCore.QRect(140, 430, 101, 31))
        font = QtGui.QFont()
        font.setFamily("CenturySchoolBook L")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_consult_disco.setFont(font)
        self.pushButton_consult_disco.setStyleSheet("QPushButton{\n"
"border-radius: 15px;\n"
"background-color: rgb(0, 21, 70);\n"
"color: rgb(255,255,255);\n"
"font-weight: bold;\n"
"font-family: CenturySchoolBook L;\n"
"font-size: 14px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(114, 159, 207);\n"
"\n"
"}")
        self.pushButton_consult_disco.setObjectName("pushButton_consult_disco")
        self.comboBox_place_disco = QtWidgets.QComboBox(Dialog)
        self.comboBox_place_disco.setGeometry(QtCore.QRect(140, 90, 241, 25))
        self.comboBox_place_disco.setStyleSheet("font-weight: bold;\n"
"font-family: Century SchoolBook L;\n"
"background-color: rgb(211, 215, 207);\n"
"color: rgb(85, 87, 83);")
        self.comboBox_place_disco.setObjectName("comboBox_place_disco")
        self.comboBox_place_disco_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_place_disco_2.setGeometry(QtCore.QRect(140, 270, 241, 25))
        self.comboBox_place_disco_2.setStyleSheet("font-weight: bold;\n"
"font-family: Century SchoolBook L;\n"
"background-color: rgb(211, 215, 207);\n"
"color: rgb(85, 87, 83);")
        self.comboBox_place_disco_2.setObjectName("comboBox_place_disco_2")
        self.label_economy_level_disco = QtWidgets.QLabel(Dialog)
        self.label_economy_level_disco.setGeometry(QtCore.QRect(140, 380, 141, 17))
        self.label_economy_level_disco.setStyleSheet("font-family: Century SchoolBook L;\n"
"color: rgb(136, 138, 133);\n"
"background: transparent;\n"
"border: none;\n"
"font-weight: bold;")
        self.label_economy_level_disco.setObjectName("label_economy_level_disco")
        self.comboBox_place_disco_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_place_disco_3.setGeometry(QtCore.QRect(140, 350, 241, 25))
        self.comboBox_place_disco_3.setStyleSheet("font-weight: bold;\n"
"font-family: Century SchoolBook L;\n"
"background-color: rgb(211, 215, 207);\n"
"color: rgb(85, 87, 83);")
        self.comboBox_place_disco_3.setObjectName("comboBox_place_disco_3")
        self.label_score_disco = QtWidgets.QLabel(Dialog)
        self.label_score_disco.setGeometry(QtCore.QRect(140, 300, 141, 17))
        self.label_score_disco.setStyleSheet("font-family: Century SchoolBook L;\n"
"color: rgb(136, 138, 133);\n"
"background: transparent;\n"
"border: none;\n"
"font-weight: bold;")
        self.label_score_disco.setObjectName("label_score_disco")
        self.label_presupuesto_disco = QtWidgets.QLabel(Dialog)
        self.label_presupuesto_disco.setGeometry(QtCore.QRect(140, 220, 141, 17))
        self.label_presupuesto_disco.setStyleSheet("font-family: Century SchoolBook L;\n"
"color: rgb(136, 138, 133);\n"
"background: transparent;\n"
"border: none;\n"
"font-weight: bold;")
        self.label_presupuesto_disco.setObjectName("label_presupuesto_disco")
        self.label_place_disco = QtWidgets.QLabel(Dialog)
        self.label_place_disco.setGeometry(QtCore.QRect(140, 130, 141, 17))
        self.label_place_disco.setStyleSheet("font-family: Century SchoolBook L;\n"
"color: rgb(136, 138, 133);\n"
"background: transparent;\n"
"border: none;\n"
"font-weight: bold;")
        self.label_place_disco.setObjectName("label_place_disco")
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(140, 180, 241, 28))
        font = QtGui.QFont()
        font.setFamily("Century SchoolBook L")
        font.setBold(False)
        font.setWeight(50)
        self.doubleSpinBox_3.setFont(font)
        self.doubleSpinBox_3.setStyleSheet("font-family: Century SchoolBook L;\n"
"background-color: rgb(211, 215, 207);\n"
"border-bottom: 1px solid #717072;\n"
"color: rgb(0, 0, 0);")
        self.doubleSpinBox_3.setMaximum(100.0)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.label_result_disco_recommended = QtWidgets.QLabel(Dialog)
        self.label_result_disco_recommended.setGeometry(QtCore.QRect(470, 110, 591, 371))
        self.label_result_disco_recommended.setStyleSheet("QLabel{\n"
"font-family: Century SchoolBook L;\n"
"border-radius: 15px;\n"
"background-color: rgb(211, 215, 207);\n"
"color: rgb(0,0,0);\n"
"}")
        self.label_result_disco_recommended.setText("")
        self.label_result_disco_recommended.setObjectName("label_result_disco_recommended")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Discoteca"))
        self.label_disco_recommended.setText(_translate("Dialog", "Discoteca/s recomendada/s:"))
        self.pushButton_consult_disco.setText(_translate("Dialog", "Consultar"))
        self.label_economy_level_disco.setText(_translate("Dialog", "Nivel económico"))
        self.label_score_disco.setText(_translate("Dialog", "Puntuación"))
        self.label_presupuesto_disco.setText(_translate("Dialog", "Presupuesto"))
        self.label_place_disco.setText(_translate("Dialog", "Lugar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

