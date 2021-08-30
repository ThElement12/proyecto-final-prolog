# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cultural_activities_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import rules_prolog.reglas as reglas


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1092, 500)
        Dialog.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(247, 209, 209, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label_result_culture = QtWidgets.QLabel(Dialog)
        self.label_result_culture.setGeometry(QtCore.QRect(510, 110, 561, 361))
        self.label_result_culture.setStyleSheet("QLabel{\n"
"font-family: Century SchoolBook L;\n"
"border-radius: 15px;\n"
"background-color: rgb(211, 215, 207);\n"
"color: rgb(0,0,0);\n"
"}")
        self.label_result_culture.setText("")
        self.label_result_culture.setObjectName("label_result_culture")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(70, 90, 91, 51))
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
        icon.addPixmap(QtGui.QPixmap("../resources/budget_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setObjectName("pushButton")
        self.label_actividad_cult = QtWidgets.QLabel(Dialog)
        self.label_actividad_cult.setGeometry(QtCore.QRect(510, 80, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setBold(True)
        font.setWeight(75)
        self.label_actividad_cult.setFont(font)
        self.label_actividad_cult.setStyleSheet("background-color: transparent;")
        self.label_actividad_cult.setObjectName("label_actividad_cult")
        self.pushButton_consult_culture = QtWidgets.QPushButton(Dialog)
        self.pushButton_consult_culture.setGeometry(QtCore.QRect(150, 170, 101, 31))
        font = QtGui.QFont()
        font.setFamily("CenturySchoolBook L")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_consult_culture.setFont(font)
        self.pushButton_consult_culture.setStyleSheet("QPushButton{\n"
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
        self.pushButton_consult_culture.setObjectName("pushButton_consult_culture")
        self.label_place_cinema = QtWidgets.QLabel(Dialog)
        self.label_place_cinema.setGeometry(QtCore.QRect(150, 130, 101, 17))
        self.label_place_cinema.setStyleSheet("font-family: Century SchoolBook L;\n"
"color: rgb(136, 138, 133);\n"
"background: transparent;\n"
"border: none;\n"
"font-weight: bold;")
        self.label_place_cinema.setObjectName("label_place_cinema")
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(150, 100, 311, 28))
        font = QtGui.QFont()
        font.setFamily("Century SchoolBook L")
        font.setBold(False)
        font.setWeight(50)
        self.doubleSpinBox_3.setFont(font)
        self.doubleSpinBox_3.setStyleSheet("font-family: Century SchoolBook L;\n"
"background-color: rgb(211, 215, 207);\n"
"border-bottom: 1px solid #717072;\n"
"color: rgb(0, 0, 0);")
        self.doubleSpinBox_3.setMaximum(100000000.0)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        self.pushButton_consult_culture.clicked.connect(self.consult_culture)

    def consult_culture(self):
        presupuesto = self.doubleSpinBox_3.value()
        result_culture = reglas.todas_las_actividades(presupuesto)
        print(result_culture)
        final_result = " "
        for restaurant in reglas.todas_las_actividades(presupuesto):
                final_result = final_result + str(restaurant) + "\n"


        self.label_result_culture.setText(str(final_result.replace('_', ' ').upper()))    


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Cultura"))
        self.label_actividad_cult.setText(_translate("Dialog", "Actividad/es recomendada/s:"))
        self.pushButton_consult_culture.setText(_translate("Dialog", "Consultar"))
        self.label_place_cinema.setText(_translate("Dialog", "Presupuesto"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

