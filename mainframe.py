# export DISPLAY=:0 - command for Qt Display Connection errors
import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainframe_gui import Ui_Form
from model import Model

class MainWindow(QMainWindow, Ui_Form):
    def __init__(self, model=None):
        self.model = model
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.connectSignals()

    def connectSignals(self):
        self.ui_dia.editingFinished.connect(self.cuttingdata_calc)        
        self.ui_speed.editingFinished.connect(self.cuttingdata_calc)
        self.ui_rev.editingFinished.connect(self.cuttingdata_calc)

    def speed_expr(self):
        self.diameter = self.ui_dia.text()
        self.rev = self.ui_rev.text()
        speed_result = self.model.speed_formel(float(self.rev), float(self.diameter))
        self.ui_speed.setText(str(speed_result))

    def rev_expr(self):
        self.diameter = self.ui_dia.text()
        self.speed = self.ui_speed.text()
        rev_result = self.model.revolutions_formel(float(self.speed), float(self.diameter))
        self.ui_rev.setText(str(rev_result))

    def cuttingdata_calc(self):
        if self.ui_dia.text()!="":
            if self.ui_speed.text()!="" or self.ui_rev.text()!="":
                if self.sender() == self.ui_speed:
                    self.rev_expr()
                if self.sender() == self.ui_rev:
                    self.speed_expr()
                self.rev_expr()
        else:
            return

if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = Model()
    mainWindow = MainWindow(model)
    mainWindow.show()
    sys.exit(app.exec_())