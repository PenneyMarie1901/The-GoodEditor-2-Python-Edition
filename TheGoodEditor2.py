from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui
import sys


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 1200, 757)
    win.setWindowTitle("The GoodEditor 2 Python Edition Version 1.0.0")
    win.setWindowIcon(QtGui.QIcon('icon.png'))
    win.show()
    sys.exit(app.exec_())


window()
