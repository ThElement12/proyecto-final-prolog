# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cinema_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1094, 545)
        Dialog.setStyleSheet("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-10, 0, 1121, 511))
        self.label.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(247, 209, 209, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label.setText("")
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(-10, 0, 1111, 551))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.comboBox_city_restaurant_4 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_city_restaurant_4.setGeometry(QtCore.QRect(120, 80, 271, 31))
        self.comboBox_city_restaurant_4.setCurrentText("")
        self.comboBox_city_restaurant_4.setObjectName("comboBox_city_restaurant_4")
        self.comboBox_city_restaurant_4.addItems(["Palacio del Cine", "Cinemacentro", "Cine Colinas Mall", "Cinemateca", "Caribbean Cinemas Fine Arts", "The Colonial Gate 4D Cinema", "Caribbean Cinemas Bavaro"])

        self.label_budget_restaurant_3 = QtWidgets.QLabel(self.tab_2)
        self.label_budget_restaurant_3.setGeometry(QtCore.QRect(120, 120, 171, 17))
        self.label_budget_restaurant_3.setStyleSheet("font-family: Century SchoolBook L;\n"
"color: rgb(136, 138, 133);\n"
"background: transparent;\n"
"border: none;\n"
"font-weight: bold;")
        self.label_budget_restaurant_3.setObjectName("label_budget_restaurant_3")
        self.pushButton_consult_cinema_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_consult_cinema_2.setGeometry(QtCore.QRect(120, 160, 101, 31))
        font = QtGui.QFont()
        font.setFamily("CenturySchoolBook L")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_consult_cinema_2.setFont(font)
        self.pushButton_consult_cinema_2.setStyleSheet("QPushButton{\n"
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
        self.pushButton_consult_cinema_2.setObjectName("pushButton_consult_cinema_2")
        self.pushButton_type_movie_icon_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_type_movie_icon_2.setGeometry(QtCore.QRect(50, 80, 49, 32))
        self.pushButton_type_movie_icon_2.setStyleSheet("QPushButton{\n"
"border-radius: 20px;\n"
"background-color: transparent;\n"
"color: rgb(0,0,0);\n"
"font-family: Century SchoolBook L;\n"
"font-weight: bold;\n"
"\n"
"}")
        self.pushButton_type_movie_icon_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resources/cinema_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_type_movie_icon_2.setIcon(icon)
        self.pushButton_type_movie_icon_2.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_type_movie_icon_2.setObjectName("pushButton_type_movie_icon_2")
        self.label_cinema_recommended_2 = QtWidgets.QLabel(self.tab_2)
        self.label_cinema_recommended_2.setGeometry(QtCore.QRect(450, 70, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setBold(True)
        font.setWeight(75)
        self.label_cinema_recommended_2.setFont(font)
        self.label_cinema_recommended_2.setStyleSheet("background-color: transparent;")
        self.label_cinema_recommended_2.setObjectName("label_cinema_recommended_2")
        self.label_result_cinema_recommended_2 = QtWidgets.QLabel(self.tab_2)
        self.label_result_cinema_recommended_2.setGeometry(QtCore.QRect(450, 110, 591, 371))
        self.label_result_cinema_recommended_2.setStyleSheet("QLabel{\n"
"font-family: Century SchoolBook L;\n"
"border-radius: 15px;\n"
"background-color: rgb(211, 215, 207);\n"
"color: rgb(0,0,0);\n"
"}")
        self.label_result_cinema_recommended_2.setText("")
        self.label_result_cinema_recommended_2.setObjectName("label_result_cinema_recommended_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.comboBox_place_cinema = QtWidgets.QComboBox(self.tab)
        self.comboBox_place_cinema.setGeometry(QtCore.QRect(130, 80, 281, 25))
        self.comboBox_place_cinema.setStyleSheet("font-weight: bold;\n"
"font-family: Century SchoolBook L;\n"
"background-color: rgb(211, 215, 207);\n"
"color: rgb(85, 87, 83);")
        self.comboBox_place_cinema.setObjectName("comboBox_place_cinema")
        self.comboBox_place_cinema.addItems(["Boca Chica", "Sosua", "Bavaro", "Punta Cana", "Las Terrenas", "Las Galeras"])

        self.label_place_cinema = QtWidgets.QLabel(self.tab)
        self.label_place_cinema.setGeometry(QtCore.QRect(130, 110, 71, 17))
        self.label_place_cinema.setStyleSheet("font-family: Century SchoolBook L;\n"
"color: rgb(136, 138, 133);\n"
"background: transparent;\n"
"border: none;\n"
"font-weight: bold;")
        self.label_place_cinema.setObjectName("label_place_cinema")
        self.comboBox_gender_cinema = QtWidgets.QComboBox(self.tab)
        self.comboBox_gender_cinema.setGeometry(QtCore.QRect(130, 140, 281, 25))
        self.comboBox_gender_cinema.setStyleSheet("font-weight: bold;\n"
"font-family: Century SchoolBook L;\n"
"background-color: rgb(211, 215, 207);\n"
"color: rgb(85, 87, 83);")
        self.comboBox_gender_cinema.setObjectName("comboBox_gender_cinema")
        self.comboBox_gender_cinema.addItems(["Terror", "Drama", "Ficcion", "Humor"])


        self.label_gender_cinema = QtWidgets.QLabel(self.tab)
        self.label_gender_cinema.setGeometry(QtCore.QRect(130, 170, 71, 17))
        self.label_gender_cinema.setStyleSheet("font-family: Century SchoolBook L;\n"
"color: rgb(136, 138, 133);\n"
"background: transparent;\n"
"border: none;\n"
"font-weight: bold;")
        self.label_gender_cinema.setObjectName("label_gender_cinema")
        self.label_cinema_recommended = QtWidgets.QLabel(self.tab)
        self.label_cinema_recommended.setGeometry(QtCore.QRect(450, 70, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setBold(True)
        font.setWeight(75)
        self.label_cinema_recommended.setFont(font)
        self.label_cinema_recommended.setStyleSheet("background-color: transparent;")
        self.label_cinema_recommended.setObjectName("label_cinema_recommended")
        self.label_result_cinema_recommended = QtWidgets.QLabel(self.tab)
        self.label_result_cinema_recommended.setGeometry(QtCore.QRect(450, 110, 591, 371))
        self.label_result_cinema_recommended.setStyleSheet("QLabel{\n"
"font-family: Century SchoolBook L;\n"
"border-radius: 15px;\n"
"background-color: rgb(211, 215, 207);\n"
"color: rgb(0,0,0);\n"
"}")
        self.label_result_cinema_recommended.setText("")
        self.label_result_cinema_recommended.setObjectName("label_result_cinema_recommended")
        self.pushButton_consult_cinema = QtWidgets.QPushButton(self.tab)
        self.pushButton_consult_cinema.setGeometry(QtCore.QRect(130, 210, 101, 31))
        font = QtGui.QFont()
        font.setFamily("CenturySchoolBook L")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_consult_cinema.setFont(font)
        self.pushButton_consult_cinema.setStyleSheet("QPushButton{\n"
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
        self.pushButton_consult_cinema.setObjectName("pushButton_consult_cinema")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(50, 70, 51, 111))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_type_movie_icon = QtWidgets.QPushButton(self.widget)
        self.pushButton_type_movie_icon.setStyleSheet("QPushButton{\n"
"border-radius: 20px;\n"
"background-color: transparent;\n"
"color: rgb(0,0,0);\n"
"font-family: Century SchoolBook L;\n"
"font-weight: bold;\n"
"\n"
"}")
        self.pushButton_type_movie_icon.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../resources/type_movie_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_type_movie_icon.setIcon(icon1)
        self.pushButton_type_movie_icon.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_type_movie_icon.setObjectName("pushButton_type_movie_icon")
        self.verticalLayout.addWidget(self.pushButton_type_movie_icon)
        self.pushButton_place_icon = QtWidgets.QPushButton(self.widget)
        self.pushButton_place_icon.setStyleSheet("QPushButton{\n"
"border-radius: 20px;\n"
"background-color: transparent;\n"
"color: rgb(0,0,0);\n"
"font-family: Century SchoolBook L;\n"
"font-weight: bold;\n"
"\n"
"}")
        self.pushButton_place_icon.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../resources/place_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_place_icon.setIcon(icon2)
        self.pushButton_place_icon.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_place_icon.setObjectName("pushButton_place_icon")
        self.verticalLayout.addWidget(self.pushButton_place_icon)
        self.tabWidget.addTab(self.tab, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Cine"))
        self.label_budget_restaurant_3.setText(_translate("Dialog", "Nombre cine"))
        self.pushButton_consult_cinema_2.setText(_translate("Dialog", "Consultar"))
        self.label_cinema_recommended_2.setText(_translate("Dialog", "Sucursal/es recomendado/s:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Consulta 2"))


        self.label_place_cinema.setText(_translate("Dialog", "Lugar"))
        self.label_gender_cinema.setText(_translate("Dialog", "Género"))
        self.label_cinema_recommended.setText(_translate("Dialog", "Cine/s recomendado/s:"))
        self.pushButton_consult_cinema.setText(_translate("Dialog", "Consultar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Consulta 1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

