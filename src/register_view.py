# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1094, 498)
        Dialog.setStyleSheet("")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(-10, 0, 1111, 501))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(520, 30, 81, 41))
        self.pushButton.setStyleSheet("QPushButton{\n"
"border-radius: 20px;\n"
"background-color: transparent;\n"
"color: rgb(0,0,0);\n"
"font-family: Century SchoolBook L;\n"
"font-weight: bold;\n"
"\n"
"}")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resources/sign_up_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(470, 150, 211, 25))
        self.comboBox.setObjectName("comboBox")
        self.label_place_disco = QtWidgets.QLabel(self.tab)
        self.label_place_disco.setGeometry(QtCore.QRect(470, 180, 141, 17))
        self.label_place_disco.setStyleSheet("font-family: Century SchoolBook L;\n"
"color: rgb(136, 138, 133);\n"
"background: transparent;\n"
"border: none;\n"
"font-weight: bold;")
        self.label_place_disco.setObjectName("label_place_disco")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.tab)
        self.doubleSpinBox.setGeometry(QtCore.QRect(470, 220, 211, 26))
        self.doubleSpinBox.setMaximum(100000000.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.label_place_disco_2 = QtWidgets.QLabel(self.tab)
        self.label_place_disco_2.setGeometry(QtCore.QRect(470, 250, 141, 17))
        self.label_place_disco_2.setStyleSheet("font-family: Century SchoolBook L;\n"
"color: rgb(136, 138, 133);\n"
"background: transparent;\n"
"border: none;\n"
"font-weight: bold;")
        self.label_place_disco_2.setObjectName("label_place_disco_2")
        self.spinBox = QtWidgets.QSpinBox(self.tab)
        self.spinBox.setGeometry(QtCore.QRect(470, 290, 211, 26))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(10)
        self.spinBox.setObjectName("spinBox")
        self.label_place_disco_3 = QtWidgets.QLabel(self.tab)
        self.label_place_disco_3.setGeometry(QtCore.QRect(470, 320, 141, 17))
        self.label_place_disco_3.setStyleSheet("font-family: Century SchoolBook L;\n"
"color: rgb(136, 138, 133);\n"
"background: transparent;\n"
"border: none;\n"
"font-weight: bold;")
        self.label_place_disco_3.setObjectName("label_place_disco_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(470, 360, 211, 25))
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"font-family: Century SchoolBook L;\n"
"color: rgb(85, 87, 83);\n"
"background: transparent;\n"
"border: none;\n"
"font-weight: bold;\n"
"border-bottom: 1px solid #717072;\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(470, 90, 211, 25))
        self.lineEdit_3.setStyleSheet("QLineEdit {\n"
"font-family: Century SchoolBook L;\n"
"color: rgb(85, 87, 83);\n"
"background: transparent;\n"
"border: none;\n"
"font-weight: bold;\n"
"border-bottom: 1px solid #717072;\n"
"}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_register_disco = QtWidgets.QPushButton(self.tab)
        self.pushButton_register_disco.setGeometry(QtCore.QRect(520, 410, 101, 31))
        font = QtGui.QFont()
        font.setFamily("CenturySchoolBook L")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_register_disco.setFont(font)
        self.pushButton_register_disco.setStyleSheet("QPushButton{\n"
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
        self.pushButton_register_disco.setObjectName("pushButton_register_disco")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 30, 81, 41))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"border-radius: 20px;\n"
"background-color: transparent;\n"
"color: rgb(0,0,0);\n"
"font-family: Century SchoolBook L;\n"
"font-weight: bold;\n"
"\n"
"}")
        self.pushButton_2.setText("")
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(470, 90, 211, 25))
        self.lineEdit_4.setStyleSheet("QLineEdit {\n"
"font-family: Century SchoolBook L;\n"
"color: rgb(85, 87, 83);\n"
"background: transparent;\n"
"border: none;\n"
"font-weight: bold;\n"
"border-bottom: 1px solid #717072;\n"
"}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(470, 150, 211, 26))
        self.doubleSpinBox_2.setMaximum(100000000.0)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.label_place_disco_4 = QtWidgets.QLabel(self.tab_2)
        self.label_place_disco_4.setGeometry(QtCore.QRect(470, 180, 141, 17))
        self.label_place_disco_4.setStyleSheet("font-family: Century SchoolBook L;\n"
"color: rgb(136, 138, 133);\n"
"background: transparent;\n"
"border: none;\n"
"font-weight: bold;")
        self.label_place_disco_4.setObjectName("label_place_disco_4")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_2.setGeometry(QtCore.QRect(470, 220, 211, 25))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_place_disco_5 = QtWidgets.QLabel(self.tab_2)
        self.label_place_disco_5.setGeometry(QtCore.QRect(470, 250, 141, 17))
        self.label_place_disco_5.setStyleSheet("font-family: Century SchoolBook L;\n"
"color: rgb(136, 138, 133);\n"
"background: transparent;\n"
"border: none;\n"
"font-weight: bold;")
        self.label_place_disco_5.setObjectName("label_place_disco_5")
        self.pushButton_register_disco_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_register_disco_2.setGeometry(QtCore.QRect(510, 290, 101, 31))
        font = QtGui.QFont()
        font.setFamily("CenturySchoolBook L")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_register_disco_2.setFont(font)
        self.pushButton_register_disco_2.setStyleSheet("QPushButton{\n"
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
        self.pushButton_register_disco_2.setObjectName("pushButton_register_disco_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_4.setGeometry(QtCore.QRect(520, 30, 81, 41))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"border-radius: 20px;\n"
"background-color: transparent;\n"
"color: rgb(0,0,0);\n"
"font-family: Century SchoolBook L;\n"
"font-weight: bold;\n"
"\n"
"}")
        self.pushButton_4.setText("")
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_6.setGeometry(QtCore.QRect(470, 90, 211, 25))
        self.lineEdit_6.setStyleSheet("QLineEdit {\n"
"font-family: Century SchoolBook L;\n"
"color: rgb(85, 87, 83);\n"
"background: transparent;\n"
"border: none;\n"
"font-weight: bold;\n"
"border-bottom: 1px solid #717072;\n"
"}")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_3.setGeometry(QtCore.QRect(470, 140, 211, 25))
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_place_disco_7 = QtWidgets.QLabel(self.tab_4)
        self.label_place_disco_7.setGeometry(QtCore.QRect(470, 170, 141, 17))
        self.label_place_disco_7.setStyleSheet("font-family: Century SchoolBook L;\n"
"color: rgb(136, 138, 133);\n"
"background: transparent;\n"
"border: none;\n"
"font-weight: bold;")
        self.label_place_disco_7.setObjectName("label_place_disco_7")
        self.spinBox_2 = QtWidgets.QSpinBox(self.tab_4)
        self.spinBox_2.setGeometry(QtCore.QRect(470, 210, 211, 26))
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(10)
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_place_disco_8 = QtWidgets.QLabel(self.tab_4)
        self.label_place_disco_8.setGeometry(QtCore.QRect(470, 240, 141, 17))
        self.label_place_disco_8.setStyleSheet("font-family: Century SchoolBook L;\n"
"color: rgb(136, 138, 133);\n"
"background: transparent;\n"
"border: none;\n"
"font-weight: bold;")
        self.label_place_disco_8.setObjectName("label_place_disco_8")
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_4.setGeometry(QtCore.QRect(470, 280, 211, 26))
        self.doubleSpinBox_4.setMaximum(100000000.0)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.label_place_disco_9 = QtWidgets.QLabel(self.tab_4)
        self.label_place_disco_9.setGeometry(QtCore.QRect(470, 310, 141, 17))
        self.label_place_disco_9.setStyleSheet("font-family: Century SchoolBook L;\n"
"color: rgb(136, 138, 133);\n"
"background: transparent;\n"
"border: none;\n"
"font-weight: bold;")
        self.label_place_disco_9.setObjectName("label_place_disco_9")
        self.pushButton_register_disco_4 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_register_disco_4.setGeometry(QtCore.QRect(510, 350, 101, 31))
        font = QtGui.QFont()
        font.setFamily("CenturySchoolBook L")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_register_disco_4.setFont(font)
        self.pushButton_register_disco_4.setStyleSheet("QPushButton{\n"
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
        self.pushButton_register_disco_4.setObjectName("pushButton_register_disco_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-20, -80, 1111, 581))
        self.label.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(247, 209, 209, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.tabWidget.raise_()

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Registrar"))
        self.label_place_disco.setText(_translate("Dialog", "Ciudad"))
        self.label_place_disco_2.setText(_translate("Dialog", "Precio"))
        self.label_place_disco_3.setText(_translate("Dialog", "Calificación"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Tipo de comida"))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog", "Nombre restaurante"))
        self.pushButton_register_disco.setText(_translate("Dialog", "Registrar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Restaurante"))
        self.lineEdit_4.setPlaceholderText(_translate("Dialog", "Nombre actividad/evento"))
        self.label_place_disco_4.setText(_translate("Dialog", "Precio"))
        self.label_place_disco_5.setText(_translate("Dialog", " Ciudad/Lugar"))
        self.pushButton_register_disco_2.setText(_translate("Dialog", "Registrar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Actividades Culturales/Eventos importantes"))
        self.lineEdit_6.setPlaceholderText(_translate("Dialog", "Nombre discoteca"))
        self.label_place_disco_7.setText(_translate("Dialog", "Ciudad"))
        self.label_place_disco_8.setText(_translate("Dialog", "Calificación"))
        self.label_place_disco_9.setText(_translate("Dialog", "Precio entrada"))
        self.pushButton_register_disco_4.setText(_translate("Dialog", "Registrar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Discoteca"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

