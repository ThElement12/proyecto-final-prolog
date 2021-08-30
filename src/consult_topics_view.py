# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'consult_topics_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from beach_view import Ui_Dialog as beach_view
from beach_view import *
from cultural_activities_view import Ui_Dialog as cultural_activity
from cinema_view import Ui_Dialog as cinema_view
from disco_view import Ui_Dialog as disco_view
from register_view import Ui_Dialog as register_view



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1094, 483)
        Form.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(247, 209, 209, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 1101, 491))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("QPushButton{\n"
"border-radius: 15px;\n"
"background-color: rgb(0, 21, 70);\n"
"color: rgb(255,255,255);\n"
"font-weight: bold;\n"
"font-family: CenturySchoolBook L;\n"
"font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(114, 159, 207);\n"
"\n"
"}")
        self.groupBox.setObjectName("groupBox")
        self.btn_cons_playas = QtWidgets.QPushButton(self.groupBox)
        self.btn_cons_playas.setGeometry(QtCore.QRect(60, 80, 201, 91))
        font = QtGui.QFont()
        font.setFamily("CenturySchoolBook L")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.btn_cons_playas.setFont(font)
        self.btn_cons_playas.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resources/restaurant_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cons_playas.setIcon(icon)
        self.btn_cons_playas.setIconSize(QtCore.QSize(32, 32))
        self.btn_cons_playas.setObjectName("btn_cons_playas")
        self.btn_cons_cines = QtWidgets.QPushButton(self.groupBox)
        self.btn_cons_cines.setGeometry(QtCore.QRect(630, 80, 181, 91))
        font = QtGui.QFont()
        font.setFamily("CenturySchoolBook L")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.btn_cons_cines.setFont(font)
        self.btn_cons_cines.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../resources/movies_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cons_cines.setIcon(icon1)
        self.btn_cons_cines.setIconSize(QtCore.QSize(32, 32))
        self.btn_cons_cines.setObjectName("btn_cons_cines")
        self.btn_cons_d = QtWidgets.QPushButton(self.groupBox)
        self.btn_cons_d.setGeometry(QtCore.QRect(860, 80, 171, 91))
        font = QtGui.QFont()
        font.setFamily("CenturySchoolBook L")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.btn_cons_d.setFont(font)
        self.btn_cons_d.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../resources/disco_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cons_d.setIcon(icon2)
        self.btn_cons_d.setIconSize(QtCore.QSize(32, 32))
        self.btn_cons_d.setObjectName("btn_cons_d")
        self.btn_cons_actividadesc = QtWidgets.QPushButton(self.groupBox)
        self.btn_cons_actividadesc.setGeometry(QtCore.QRect(310, 80, 271, 91))
        font = QtGui.QFont()
        font.setFamily("CenturySchoolBook L")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.btn_cons_actividadesc.setFont(font)
        self.btn_cons_actividadesc.setStyleSheet("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../resources/cultural_act_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cons_actividadesc.setIcon(icon3)
        self.btn_cons_actividadesc.setIconSize(QtCore.QSize(32, 32))
        self.btn_cons_actividadesc.setObjectName("btn_cons_actividadesc")
        self.btn_cons_eventosi_2 = QtWidgets.QPushButton(self.groupBox)
        self.btn_cons_eventosi_2.setGeometry(QtCore.QRect(430, 240, 241, 91))
        font = QtGui.QFont()
        font.setFamily("CenturySchoolBook L")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.btn_cons_eventosi_2.setFont(font)
        self.btn_cons_eventosi_2.setStyleSheet("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../resources/sign_up_white_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cons_eventosi_2.setIcon(icon4)
        self.btn_cons_eventosi_2.setIconSize(QtCore.QSize(32, 32))
        self.btn_cons_eventosi_2.setObjectName("btn_cons_eventosi_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.btn_cons_playas.clicked.connect(self.connect_to_restaurants)
        self.btn_cons_actividadesc.clicked.connect(self.connect_to_culture)
        self.btn_cons_cines.clicked.connect(self.connect_to_cinema)
        self.btn_cons_d.clicked.connect(self.connect_to_disco)
        self.btn_cons_eventosi_2.clicked.connect(self.connect_to_register)



    def connect_to_restaurants(self):
        self.Form = QtWidgets.QWidget()
        self.ui = beach_view()
        self.ui.setupUi(self.Form) 
        self.Form.show()

    def connect_to_culture(self):
        self.Form = QtWidgets.QWidget()
        self.ui = cultural_activity()
        self.ui.setupUi(self.Form) 
        self.Form.show()

    def connect_to_cinema(self):
        self.Form = QtWidgets.QWidget()
        self.ui = cinema_view()
        self.ui.setupUi(self.Form) 
        self.Form.show()

    def connect_to_disco(self):
        self.Form = QtWidgets.QWidget()
        self.ui = disco_view()
        self.ui.setupUi(self.Form) 
        self.Form.show()

    def connect_to_register(self):
        self.Form = QtWidgets.QWidget()
        self.ui = register_view()
        self.ui.setupUi(self.Form) 
        self.Form.show()



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", " Temas"))
        self.groupBox.setTitle(_translate("Form", "Selecciona un tema para consultar"))
        self.btn_cons_playas.setText(_translate("Form", "  Restaurantes"))
        self.btn_cons_cines.setText(_translate("Form", "  Cines"))
        self.btn_cons_d.setText(_translate("Form", "  Discotecas"))
        self.btn_cons_actividadesc.setText(_translate("Form", "Actividades Culturales"))
        self.btn_cons_eventosi_2.setText(_translate("Form", "  Registrar"))

import image_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

