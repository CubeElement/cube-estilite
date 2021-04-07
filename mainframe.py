# export DISPLAY=:0 - command for Qt Display Connection errors
import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainframe_gui import Ui_Form

class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Ui_Form()
    mainWindow = QMainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())