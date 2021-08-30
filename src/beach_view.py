# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'beach_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1093, 541)
        Dialog.setStyleSheet("")
        self.tabWidget_2 = QtWidgets.QTabWidget(Dialog)
        self.tabWidget_2.setGeometry(QtCore.QRect(-10, 0, 1111, 561))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setStyleSheet("QPushButton{\n"
"border-radius: 20px;\n"
"background-color: transparent;\n"
"color: rgb(0,0,0);\n"
"font-family: Century SchoolBook L;\n"
"font-weight: bold;\n"
"\n"
"}")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.widget = QtWidgets.QWidget(self.tab_2)
        self.widget.setGeometry(QtCore.QRect(70, 60, 71, 311))
        self.widget.setObjectName("widget")
        self.verticalLayout_icons = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_icons.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_icons.setObjectName("verticalLayout_icons")
        self.pushButton_budgetIcon = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Century SchoolBook L")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_budgetIcon.setFont(font)
        self.pushButton_budgetIcon.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resources/budget_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_budgetIcon.setIcon(icon)
        self.pushButton_budgetIcon.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_budgetIcon.setObjectName("pushButton_budgetIcon")
        self.verticalLayout_icons.addWidget(self.pushButton_budgetIcon)
        self.pushButton_cityIcon = QtWidgets.QPushButton(self.widget)
        self.pushButton_cityIcon.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../resources/city_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_cityIcon.setIcon(icon1)
        self.pushButton_cityIcon.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_cityIcon.setObjectName("pushButton_cityIcon")
        self.verticalLayout_icons.addWidget(self.pushButton_cityIcon)
        self.pushButton_economyIcon = QtWidgets.QPushButton(self.widget)
        self.pushButton_economyIcon.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../resources/economy_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_economyIcon.setIcon(icon2)
        self.pushButton_economyIcon.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_economyIcon.setObjectName("pushButton_economyIcon")
        self.verticalLayout_icons.addWidget(self.pushButton_economyIcon)
        self.pushButton_foodIcon = QtWidgets.QPushButton(self.widget)
        self.pushButton_foodIcon.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../resources/food_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_foodIcon.setIcon(icon3)
        self.pushButton_foodIcon.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_foodIcon.setObjectName("pushButton_foodIcon")
        self.verticalLayout_icons.addWidget(self.pushButton_foodIcon)
        self.pushButton_porcentageIcon = QtWidgets.QPushButton(self.widget)
        self.pushButton_porcentageIcon.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../resources/porcentage_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_porcentageIcon.setIcon(icon4)
        self.pushButton_porcentageIcon.setIconSize(QtCore.QSize(28, 28))
        self.pushButton_porcentageIcon.setObjectName("pushButton_porcentageIcon")
        self.verticalLayout_icons.addWidget(self.pushButton_porcentageIcon)
        self.label_budget_restaurant = QtWidgets.QLabel(self.tab_2)
        self.label_budget_restaurant.setGeometry(QtCore.QRect(160, 110, 101, 17))
        self.label_budget_restaurant.setStyleSheet("font-family: Century SchoolBook L;\n"
"color: rgb(136, 138, 133);\n"
"background: transparent;\n"
"border: none;\n"
"font-weight: bold;")
        self.label_budget_restaurant.setObjectName("label_budget_restaurant")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_3.setGeometry(QtCore.QRect(160, 260, 311, 30))
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_economy_level_restaurant = QtWidgets.QLabel(self.tab_2)
        self.label_economy_level_restaurant.setGeometry(QtCore.QRect(160, 230, 131, 17))
        self.label_economy_level_restaurant.setStyleSheet("font-family: Century SchoolBook L;\n"
"color: rgb(136, 138, 133);\n"
"background: transparent;\n"
"border: none;\n"
"font-weight: bold;")
        self.label_economy_level_restaurant.setObjectName("label_economy_level_restaurant")
        self.label_type_of_food_restaurant = QtWidgets.QLabel(self.tab_2)
        self.label_type_of_food_restaurant.setGeometry(QtCore.QRect(160, 290, 121, 17))
        self.label_type_of_food_restaurant.setStyleSheet("font-family: Century SchoolBook L;\n"
"color: rgb(136, 138, 133);\n"
"background: transparent;\n"
"border: none;\n"
"font-weight: bold;")
        self.label_type_of_food_restaurant.setObjectName("label_type_of_food_restaurant")
        self.comboBox_city_restaurant = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_city_restaurant.setGeometry(QtCore.QRect(160, 200, 311, 30))
        self.comboBox_city_restaurant.setCurrentText("")
        self.comboBox_city_restaurant.setObjectName("comboBox_city_restaurant")
        self.label_city_restaurant = QtWidgets.QLabel(self.tab_2)
        self.label_city_restaurant.setGeometry(QtCore.QRect(160, 170, 61, 17))
        self.label_city_restaurant.setStyleSheet("font-family: Century SchoolBook L;\n"
"color: rgb(136, 138, 133);\n"
"background: transparent;\n"
"border: none;\n"
"font-weight: bold;")
        self.label_city_restaurant.setObjectName("label_city_restaurant")
        self.label_porcentage_restaurant = QtWidgets.QLabel(self.tab_2)
        self.label_porcentage_restaurant.setGeometry(QtCore.QRect(160, 350, 91, 17))
        self.label_porcentage_restaurant.setStyleSheet("font-family: Century SchoolBook L;\n"
"color: rgb(136, 138, 133);\n"
"background: transparent;\n"
"border: none;\n"
"font-weight: bold;")
        self.label_porcentage_restaurant.setObjectName("label_porcentage_restaurant")
        self.label_restaurant = QtWidgets.QLabel(self.tab_2)
        self.label_restaurant.setGeometry(QtCore.QRect(490, 60, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setBold(True)
        font.setWeight(75)
        self.label_restaurant.setFont(font)
        self.label_restaurant.setStyleSheet("background-color: transparent;")
        self.label_restaurant.setObjectName("label_restaurant")
        self.pushButton_consult_restaurant = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_consult_restaurant.setGeometry(QtCore.QRect(160, 390, 101, 31))
        font = QtGui.QFont()
        font.setFamily("CenturySchoolBook L")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_consult_restaurant.setFont(font)
        self.pushButton_consult_restaurant.setStyleSheet("QPushButton{\n"
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
        self.pushButton_consult_restaurant.setObjectName("pushButton_consult_restaurant")
        self.comboBox_city_restaurant_2 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_city_restaurant_2.setGeometry(QtCore.QRect(160, 140, 311, 31))
        self.comboBox_city_restaurant_2.setCurrentText("")
        self.comboBox_city_restaurant_2.setObjectName("comboBox_city_restaurant_2")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(160, 80, 311, 28))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setBold(False)
        font.setWeight(50)
        self.doubleSpinBox_2.setFont(font)
        self.doubleSpinBox_2.setStyleSheet("")
        self.doubleSpinBox_2.setMaximum(100.0)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(160, 320, 311, 28))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setBold(False)
        font.setWeight(50)
        self.doubleSpinBox_3.setFont(font)
        self.doubleSpinBox_3.setStyleSheet("")
        self.doubleSpinBox_3.setMaximum(100.0)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.label_result_disco_recommended_2 = QtWidgets.QLabel(self.tab_2)
        self.label_result_disco_recommended_2.setGeometry(QtCore.QRect(490, 110, 591, 371))
        self.label_result_disco_recommended_2.setStyleSheet("QLabel{\n"
"font-family: Century SchoolBook L;\n"
"border-radius: 15px;\n"
"background-color: rgb(211, 215, 207);\n"
"color: rgb(0,0,0);\n"
"}")
        self.label_result_disco_recommended_2.setText("")
        self.label_result_disco_recommended_2.setObjectName("label_result_disco_recommended_2")
        self.label_budget_restaurant.raise_()
        self.comboBox_3.raise_()
        self.label_economy_level_restaurant.raise_()
        self.label_type_of_food_restaurant.raise_()
        self.comboBox_city_restaurant.raise_()
        self.label_city_restaurant.raise_()
        self.label_porcentage_restaurant.raise_()
        self.pushButton_consult_restaurant.raise_()
        self.comboBox_city_restaurant_2.raise_()
        self.doubleSpinBox_2.raise_()
        self.label_restaurant.raise_()
        self.doubleSpinBox_3.raise_()
        self.label_result_disco_recommended_2.raise_()
        self.tabWidget_2.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.comboBox_name_of_restaurant = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_name_of_restaurant.setGeometry(QtCore.QRect(180, 70, 271, 31))
        self.comboBox_name_of_restaurant.setCurrentText("")
        self.comboBox_name_of_restaurant.setObjectName("comboBox_name_of_restaurant")
        self.label_name_of_restaurant = QtWidgets.QLabel(self.tab_4)
        self.label_name_of_restaurant.setGeometry(QtCore.QRect(180, 110, 171, 17))
        self.label_name_of_restaurant.setStyleSheet("font-family: Century SchoolBook L;\n"
"color: rgb(136, 138, 133);\n"
"background: transparent;\n"
"border: none;\n"
"font-weight: bold;")
        self.label_name_of_restaurant.setObjectName("label_name_of_restaurant")
        self.pushButton_foodIcon_restaurant_2 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_foodIcon_restaurant_2.setGeometry(QtCore.QRect(110, 70, 69, 32))
        self.pushButton_foodIcon_restaurant_2.setText("")
        self.pushButton_foodIcon_restaurant_2.setIcon(icon3)
        self.pushButton_foodIcon_restaurant_2.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_foodIcon_restaurant_2.setObjectName("pushButton_foodIcon_restaurant_2")
        self.pushButton_consult_restaurant_2 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_consult_restaurant_2.setGeometry(QtCore.QRect(180, 150, 101, 31))
        font = QtGui.QFont()
        font.setFamily("CenturySchoolBook L")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_consult_restaurant_2.setFont(font)
        self.pushButton_consult_restaurant_2.setStyleSheet("QPushButton{\n"
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
        self.pushButton_consult_restaurant_2.setObjectName("pushButton_consult_restaurant_2")
        self.label_restaurant_2 = QtWidgets.QLabel(self.tab_4)
        self.label_restaurant_2.setGeometry(QtCore.QRect(490, 50, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setBold(True)
        font.setWeight(75)
        self.label_restaurant_2.setFont(font)
        self.label_restaurant_2.setStyleSheet("background-color: transparent;")
        self.label_restaurant_2.setObjectName("label_restaurant_2")
        self.label_result_restaurant_recommended = QtWidgets.QLabel(self.tab_4)
        self.label_result_restaurant_recommended.setGeometry(QtCore.QRect(490, 100, 591, 371))
        self.label_result_restaurant_recommended.setStyleSheet("QLabel{\n"
"font-family: Century SchoolBook L;\n"
"border-radius: 15px;\n"
"background-color: rgb(211, 215, 207);\n"
"color: rgb(0,0,0);\n"
"}")
        self.label_result_restaurant_recommended.setText("")
        self.label_result_restaurant_recommended.setObjectName("label_result_restaurant_recommended")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_budget_restaurant_3 = QtWidgets.QLabel(self.tab)
        self.label_budget_restaurant_3.setGeometry(QtCore.QRect(190, 110, 171, 17))
        self.label_budget_restaurant_3.setStyleSheet("font-family: Century SchoolBook L;\n"
"color: rgb(136, 138, 133);\n"
"background: transparent;\n"
"border: none;\n"
"font-weight: bold;")
        self.label_budget_restaurant_3.setObjectName("label_budget_restaurant_3")
        self.comboBox_city_restaurant_4 = QtWidgets.QComboBox(self.tab)
        self.comboBox_city_restaurant_4.setGeometry(QtCore.QRect(190, 70, 271, 31))
        self.comboBox_city_restaurant_4.setCurrentText("")
        self.comboBox_city_restaurant_4.setObjectName("comboBox_city_restaurant_4")
        self.pushButton_budget_icon = QtWidgets.QPushButton(self.tab)
        self.pushButton_budget_icon.setGeometry(QtCore.QRect(100, 150, 91, 51))
        self.pushButton_budget_icon.setStyleSheet("QPushButton{\n"
"border-radius: 20px;\n"
"background-color: transparent;\n"
"color: rgb(0,0,0);\n"
"font-family: Century SchoolBook L;\n"
"font-weight: bold;\n"
"\n"
"}")
        self.pushButton_budget_icon.setText("")
        self.pushButton_budget_icon.setIcon(icon)
        self.pushButton_budget_icon.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_budget_icon.setObjectName("pushButton_budget_icon")
        self.label_budget_restaurant_4 = QtWidgets.QLabel(self.tab)
        self.label_budget_restaurant_4.setGeometry(QtCore.QRect(190, 190, 171, 17))
        self.label_budget_restaurant_4.setStyleSheet("font-family: Century SchoolBook L;\n"
"color: rgb(136, 138, 133);\n"
"background: transparent;\n"
"border: none;\n"
"font-weight: bold;")
        self.label_budget_restaurant_4.setObjectName("label_budget_restaurant_4")
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.tab)
        self.doubleSpinBox_4.setGeometry(QtCore.QRect(190, 160, 271, 28))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setBold(False)
        font.setWeight(50)
        self.doubleSpinBox_4.setFont(font)
        self.doubleSpinBox_4.setStyleSheet("")
        self.doubleSpinBox_4.setMaximum(100.0)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.spinBox_hour_restaurant_3 = QtWidgets.QSpinBox(self.tab)
        self.spinBox_hour_restaurant_3.setGeometry(QtCore.QRect(190, 250, 271, 26))
        self.spinBox_hour_restaurant_3.setObjectName("spinBox_hour_restaurant_3")
        self.label_hour_restaurant_3 = QtWidgets.QLabel(self.tab)
        self.label_hour_restaurant_3.setGeometry(QtCore.QRect(190, 280, 171, 17))
        self.label_hour_restaurant_3.setStyleSheet("font-family: Century SchoolBook L;\n"
"color: rgb(136, 138, 133);\n"
"background: transparent;\n"
"border: none;\n"
"font-weight: bold;")
        self.label_hour_restaurant_3.setObjectName("label_hour_restaurant_3")
        self.pushButton_event_icon = QtWidgets.QPushButton(self.tab)
        self.pushButton_event_icon.setGeometry(QtCore.QRect(100, 60, 91, 51))
        self.pushButton_event_icon.setStyleSheet("QPushButton{\n"
"border-radius: 20px;\n"
"background-color: transparent;\n"
"color: rgb(0,0,0);\n"
"font-family: Century SchoolBook L;\n"
"font-weight: bold;\n"
"\n"
"}")
        self.pushButton_event_icon.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../resources/event_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_event_icon.setIcon(icon5)
        self.pushButton_event_icon.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_event_icon.setObjectName("pushButton_event_icon")
        self.pushButton_hour_icon = QtWidgets.QPushButton(self.tab)
        self.pushButton_hour_icon.setGeometry(QtCore.QRect(100, 240, 91, 51))
        self.pushButton_hour_icon.setStyleSheet("QPushButton{\n"
"border-radius: 20px;\n"
"background-color: transparent;\n"
"color: rgb(0,0,0);\n"
"font-family: Century SchoolBook L;\n"
"font-weight: bold;\n"
"\n"
"}")
        self.pushButton_hour_icon.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../resources/hour_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_hour_icon.setIcon(icon6)
        self.pushButton_hour_icon.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_hour_icon.setObjectName("pushButton_hour_icon")
        self.pushButton_consult_restaurant_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_consult_restaurant_3.setGeometry(QtCore.QRect(190, 320, 101, 31))
        font = QtGui.QFont()
        font.setFamily("CenturySchoolBook L")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_consult_restaurant_3.setFont(font)
        self.pushButton_consult_restaurant_3.setStyleSheet("QPushButton{\n"
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
        self.pushButton_consult_restaurant_3.setObjectName("pushButton_consult_restaurant_3")
        self.label_recommended_restaurant_3 = QtWidgets.QLabel(self.tab)
        self.label_recommended_restaurant_3.setGeometry(QtCore.QRect(490, 50, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setBold(True)
        font.setWeight(75)
        self.label_recommended_restaurant_3.setFont(font)
        self.label_recommended_restaurant_3.setStyleSheet("background-color: transparent;")
        self.label_recommended_restaurant_3.setObjectName("label_recommended_restaurant_3")
        self.label_result_disco_recommended = QtWidgets.QLabel(self.tab)
        self.label_result_disco_recommended.setGeometry(QtCore.QRect(490, 100, 591, 371))
        self.label_result_disco_recommended.setStyleSheet("QLabel{\n"
"font-family: Century SchoolBook L;\n"
"border-radius: 15px;\n"
"background-color: rgb(211, 215, 207);\n"
"color: rgb(0,0,0);\n"
"}")
        self.label_result_disco_recommended.setText("")
        self.label_result_disco_recommended.setObjectName("label_result_disco_recommended")
        self.tabWidget_2.addTab(self.tab, "")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 1111, 541))
        self.label.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(247, 209, 209, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.tabWidget_2.raise_()

        self.retranslateUi(Dialog)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Restaurantes"))
        self.label_budget_restaurant.setText(_translate("Dialog", "Presupuesto"))
        self.label_economy_level_restaurant.setText(_translate("Dialog", "Nivel económico"))
        self.label_type_of_food_restaurant.setText(_translate("Dialog", "Tipo de comida"))
        self.label_city_restaurant.setText(_translate("Dialog", "Ciudad"))
        self.label_porcentage_restaurant.setText(_translate("Dialog", "Porcentaje"))
        self.label_restaurant.setText(_translate("Dialog", "Restaurante/s recomendado/s:"))
        self.pushButton_consult_restaurant.setText(_translate("Dialog", "Consultar"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("Dialog", "Consulta 1"))
        self.label_name_of_restaurant.setText(_translate("Dialog", "Nombre restaurante"))
        self.pushButton_consult_restaurant_2.setText(_translate("Dialog", "Consultar"))
        self.label_restaurant_2.setText(_translate("Dialog", "Sector/es restaurante/s:"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("Dialog", "Consulta 2"))
        self.label_budget_restaurant_3.setText(_translate("Dialog", "Nombre evento"))
        self.label_budget_restaurant_4.setText(_translate("Dialog", "Presupuesto"))
        self.label_hour_restaurant_3.setText(_translate("Dialog", "Hora restaurante"))
        self.pushButton_consult_restaurant_3.setText(_translate("Dialog", "Consultar"))
        self.label_recommended_restaurant_3.setText(_translate("Dialog", "Restaurante/s recomendado/s:"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("Dialog", "Consulta 3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

