from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5 import uic
import sys

class load_views(QMainWindow):
    def __init__(self) -> None:
        super(load_views, self).__init__()
        uic.loadUi("home_view.ui", self)
        self.show()

application = QApplication(sys.argv)
load_view = load_views()
application.exec_()


        