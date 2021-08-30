import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow

from mainframe_gui import Ui_Form
from model import Model

import re

# export DISPLAY=:0 - command for Qt Display Connection
def display_start_fix():
    os.environ['DISPLAY'] = ':0'


class MainWindow(QMainWindow, Ui_Form):
    def __init__(self, model=None):
        self.model = model
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.actvalues = dict()
        self.actdict = self.actvalues.keys()
        self.material_data = self.model.create_cuttingdata()
        self.connectSignals()

    def connectSignals(self):
        self.ui_dia.editingFinished.connect(self.diameter_slot)
        self.ui_speed.editingFinished.connect(self.speed_slot)
        self.ui_rev.editingFinished.connect(self.rev_slot)
        self.ui_z.editingFinished.connect(self.z_slot)
        self.ui_feedrate.editingFinished.connect(self.F_slot)
        self.ui_feedpertooth.editingFinished.connect(self.f_slot)
        #############################
        self.ui_mat_p.clicked.connect(lambda x: self.materials_slot("P"))
        self.ui_mat_m.clicked.connect(lambda x: self.materials_slot("M"))
        self.ui_mat_k.clicked.connect(lambda x: self.materials_slot("K"))
        self.ui_mat_n.clicked.connect(lambda x: self.materials_slot("N"))
        self.ui_mat_s.clicked.connect(lambda x: self.materials_slot("S"))
        self.ui_mat_h.clicked.connect(lambda x: self.materials_slot("H"))

    def activate(self, name:str, value:str):
        self.actvalues[name] = float(value)
        print(f'actual values: {self.actvalues}')
            
        
    def deactivate(self, name:str=None):
        if name in self.actvalues.keys():
            del self.actvalues[name]
            print(f'actual values: {self.actvalues}')
        else:
            pass
    
    def is_valid_float(self, value=None) -> bool():
        float_regex = "([0-9]+([.][0-9]*)?|[.][0-9]+)$"
        is_float = re.match(float_regex, str(value))
        if is_float is not None:
            return True
        return False

    def assign_value(self, lineobject, value=None):
        name = lineobject.objectName()
        if value is None:
            value = lineobject.text()

        if self.is_valid_float(value) and float(value)>0 and value!="":
            print(f'{name} is equal {value}')
            lineobject.setText(str(value))
            self.activate(name, value)
        else:
            lineobject.setText("")
            self.deactivate(name)

    def diameter_slot(self):
        self.assign_value(self.ui_dia)
        self.rev_expr()

    def speed_slot(self):
        self.assign_value(self.ui_speed)
        self.rev_expr()
        self.f_slot()

    def rev_slot(self):
        self.assign_value(self.ui_rev)
        self.speed_expr()

    def z_slot(self):
        self.assign_value(self.ui_z)
        self.feedrate_expr()

    def F_slot(self):
        self.assign_value(self.ui_feedrate)
        self.feedpertooth_expr()
        self.rev_expr()

    def f_slot(self):
        self.assign_value(self.ui_feedpertooth)
        self.feedrate_expr()

    def speed_expr(self):
        if {"ui_dia", "ui_rev"}.issubset(self.actdict):
            speed_result = self.model.speed_formula(
                                                self.actvalues['ui_rev'],
                                                self.actvalues['ui_dia'])
            self.assign_value(self.ui_speed, speed_result)

    def rev_expr(self):
        if {"ui_dia", "ui_speed"}.issubset(self.actdict):
            rev_result = self.model.revolutions_formula(
                                                self.actvalues['ui_speed'],
                                                self.actvalues['ui_dia'])
            self.assign_value(self.ui_rev, rev_result)

    def feedrate_expr(self):
        if {"ui_rev", "ui_z", "ui_feedpertooth"}.issubset(self.actdict):
            feedrate_result = self.model.feedrate_formula(
                                                self.actvalues['ui_rev'],
                                                self.actvalues['ui_z'],
                                                self.actvalues['ui_feedpertooth'])
            self.assign_value(self.ui_feedrate, feedrate_result)

    def feedpertooth_expr(self):
        if {"ui_rev", "ui_z", "ui_feedrate"}.issubset(self.actdict):
            feedpertooth_result = self.model.feedpertooth_formula(
                                                self.actvalues['ui_rev'],
                                                self.actvalues['ui_z'],
                                                self.actvalues['ui_feedrate'])
            self.assign_value(self.ui_feedpertooth, feedpertooth_result)

    def materials_slot(self, material: str):
        speed = str(self.material_data[material][0])
        self.assign_value(self.ui_speed, speed)
        feedpertooth = str(self.material_data[material][1])
        self.assign_value(self.ui_feedpertooth, feedpertooth)
        self.rev_expr()
        self.feedrate_expr()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = Model()
    mainWindow = MainWindow(model)
    mainWindow.show()
    sys.exit(app.exec_())
