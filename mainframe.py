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
        self.set_current_values()
        self.actives_set = set()
        self.connectSignals()

    def set_current_values(self):
        self.diameter = self.ui_dia.text()
        self.rev = self.ui_rev.text()
        self.speed = self.ui_speed.text()
        self.feedrate = self.ui_feedrate.text()
        self.feedpertooth = self.ui_feedpertooth.text()
        self.znum = self.ui_z.text()

    def connectSignals(self):
        self.ui_dia.editingFinished.connect(self.diameter_slot)        
        self.ui_speed.editingFinished.connect(self.speed_slot)
        self.ui_rev.editingFinished.connect(self.rev_slot)
        self.ui_z.editingFinished.connect(self.z_slot)
        self.ui_feedrate.editingFinished.connect(self.F_slot)
        self.ui_feedpertooth.editingFinished.connect(self.f_slot)
    
    def update_status(self, name=None, value=None):
        if value!="" and name not in self.actives_set:
            self.actives_set.add(str(name))
        elif value=="" and name in self.actives_set:
            self.actives_set.remove(name)
        print("updated", self.actives_set)

    def user_defined(self):
        self.name = self.sender().objectName()
        self.value = self.sender().text()
        self.update_status(self.name, self.value)

    def diameter_slot(self):
        self.user_defined()
        self.diameter = self.ui_dia.text()
        self.rev_expr()
    
    def speed_slot(self):
        self.user_defined()
        self.speed = self.ui_speed.text()
        self.rev_expr()

    def rev_slot(self):
        self.user_defined()
        self.rev = self.ui_rev.text()
        self.speed_expr()

    def z_slot(self):
        self.user_defined()
        self.znum = self.ui_z.text()
        self.feedrate_expr()

    def F_slot(self):
        self.user_defined()
        self.feedrate = self.ui_feedrate.text()
        self.feedpertooth_expr()

    def f_slot(self):
        self.user_defined()
        self.feedpertooth = self.ui_feedpertooth.text()
        self.feedrate_expr()

    def speed_expr(self):
        if {"ui_dia", "ui_rev"}.issubset(self.actives_set):
            speed_result = self.model.speed_formel(self.rev, self.diameter)
            self.ui_speed.setText(str(speed_result))
            self.update_status('ui_speed', speed_result)
            print("Calc Speed", self.actives_set)
        else:
            return

    def rev_expr(self):
        if {"ui_dia", "ui_speed"}.issubset(self.actives_set): 
            rev_result = self.model.revolutions_formel(self.speed, self.diameter)
            self.ui_rev.setText(str(rev_result))
            self.update_status('ui_rev', rev_result)
            print("Calc Rev", self.actives_set)
        else:
            return

    def feedrate_expr(self):
        if {"ui_rev", "ui_z", "ui_feedpertooth"}.issubset(self.actives_set): 
            feedrate_result = self.model.feedrate_formel(self.rev, 
                                                         self.feedpertooth, 
                                                         self.znum)
            self.ui_feedrate.setText(str(feedrate_result))
            self.update_status('ui_feedrate', feedrate_result)
            print("Calc F", self.actives_set)
        else:
            return

    def feedpertooth_expr(self):
        if {"ui_rev", "ui_z", "ui_feedrate"}.issubset(self.actives_set): 
            feedpertooth_result = self.model.feedpertooth_formel(self.rev, 
                                                                 self.feedrate, 
                                                                 self.znum)
            self.ui_feedpertooth.setText(str(feedpertooth_result))
            self.update_status('ui_feedpertooth', feedpertooth_result)
            print("Calc f", self.actives_set)
        else:
            return

if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = Model()
    mainWindow = MainWindow(model)
    mainWindow.show()
    sys.exit(app.exec_())