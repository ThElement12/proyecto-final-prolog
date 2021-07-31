from home_view import *
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
#In here, we are going to connect the interfaces when button clicked. 

class connect_views(Ui_Form):
    def __init__(self, window) -> None:
        self.setupUi(window)
        self.btn_consultar.clicked.connect(self.clicked)

    def clicked(self):

        #show message to see that button is working
        print("Button is connected")
        #We can then call the other windows here
        #I open the same window but we are going to replace it we the second one. 
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form() #Here we replace it w the second windows class name and that's all.
        self.ui.setupUi(self.window)
        self.window.show()

app= QtWidgets.QApplication(sys.argv)
win = QtWidgets.QMainWindow()
ui = connect_views(win)
win.show()
app.exec_()