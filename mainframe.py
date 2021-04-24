# export DISPLAY=:0 - command for Qt Display Connection errors
import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainframe_gui import Ui_Form
from model import Model

def display_start_fix():
    os.environ['DISPLAY'] = ':0' 

class MainWindow(QMainWindow, Ui_Form):
    def __init__(self, model=None):
        self.model = model
        QMainWindow.__init__(self)
        self.setupUi(self)        
        self.set_current_values()
        self.actives_set = set()
        self.material_data = self.model.create_cuttingdata()
        self.connectSignals()

    def set_current_values(self):
        self.dia = self.ui_dia.text() # Tool diameter, mm
        self.rpm = self.ui_rev.text() # Revolutions per minute, 1/min
        self.speed = self.ui_speed.text() # Cutting speed, m/min
        self.feedrate = self.ui_feedrate.text() # Feedrate, mm/min
        self.feedpertooth = self.ui_feedpertooth.text()# Feed per Tooth, mm/tooth
        self.znum = self.ui_z.text() # Number of Teeth

    def connectSignals(self):
        self.ui_dia.editingFinished.connect(self.diameter_slot)        
        self.ui_speed.editingFinished.connect(self.speed_slot)
        self.ui_rev.editingFinished.connect(self.rev_slot)
        self.ui_z.editingFinished.connect(self.z_slot)
        self.ui_feedrate.editingFinished.connect(self.F_slot)
        self.ui_feedpertooth.editingFinished.connect(self.f_slot)

        self.ui_mat_p.clicked.connect(lambda x: self.materials_slot("P"))
        self.ui_mat_m.clicked.connect(lambda x: self.materials_slot("M"))
        self.ui_mat_k.clicked.connect(lambda x: self.materials_slot("K"))
        self.ui_mat_n.clicked.connect(lambda x: self.materials_slot("N"))
        self.ui_mat_s.clicked.connect(lambda x: self.materials_slot("S"))
        self.ui_mat_h.clicked.connect(lambda x: self.materials_slot("H"))
    
    def update_status(self, name=None, value=None):
        if value!="" and name not in self.actives_set:
            self.actives_set.add(str(name))
        elif value=="" and name in self.actives_set:
            self.actives_set.remove(name)

    def store_userinput(self):
        self.name = self.sender().objectName()
        self.value = self.sender().text()
        self.update_status(self.name, self.value)
        print(self.dia, self.rpm, self.speed, self.feedrate, self.feedpertooth, self.znum)

    def diameter_slot(self):
        self.store_userinput()
        self.dia = self.ui_dia.text()
        self.rev_expr()
    
    def speed_slot(self):
        self.store_userinput()
        self.speed = self.ui_speed.text()
        self.rev_expr()

    def rev_slot(self):
        self.store_userinput()
        self.rpm = self.ui_rev.text()
        self.speed_expr()

    def z_slot(self):
        self.store_userinput()
        self.znum = self.ui_z.text()
        self.feedrate_expr()

    def F_slot(self):
        self.store_userinput()
        self.feedrate = self.ui_feedrate.text()
        self.feedpertooth_expr()

    def f_slot(self):
        self.store_userinput()
        self.feedpertooth = self.ui_feedpertooth.text()
        self.feedrate_expr()

    def speed_expr(self):
        if {"ui_dia", "ui_rev"}.issubset(self.actives_set):
            speed_result = self.model.speed_formel(self.rpm, self.dia)
            self.ui_speed.setText(str(speed_result))
            self.speed = self.ui_speed.text()
            self.update_status('ui_speed', speed_result)

    def rev_expr(self):
        if {"ui_dia", "ui_speed"}.issubset(self.actives_set):
            self.set_current_values()
            rev_result = self.model.revolutions_formel(self.speed, self.dia)
            self.ui_rev.setText(str(rev_result))
            self.rpm = self.ui_rev.text()
            self.update_status('ui_rev', rev_result)
        else:
            return

    def feedrate_expr(self):
        if {"ui_rev", "ui_z", "ui_feedpertooth"}.issubset(self.actives_set):
            feedrate_result = self.model.feedrate_formel(self.rpm, 
                                                         self.feedpertooth, 
                                                         self.znum)
            self.ui_feedrate.setText(str(feedrate_result))
            self.feedrate = self.ui_feedrate.text()
            self.update_status('ui_feedrate', feedrate_result)
        else:
            return

    def feedpertooth_expr(self):
        if {"ui_rev", "ui_z", "ui_feedrate"}.issubset(self.actives_set): 
            feedpertooth_result = self.model.feedpertooth_formel(self.rpm, 
                                                                 self.feedrate, 
                                                                 self.znum)
            self.ui_feedpertooth.setText(str(feedpertooth_result))
            self.feedpertooth = self.ui_feedpertooth.text()
            self.update_status('ui_feedpertooth', feedpertooth_result)
        else:
            return

    def materials_slot(self, material):
        print(material)
        self.speed = self.material_data[material][0]
        self.update_status('ui_speed', self.speed)
        self.ui_speed.setText(str(self.speed))
        self.feedpertooth = self.material_data[material][1]
        self.update_status('ui_feedpertooth', self.feedpertooth)
        self.ui_feedpertooth.setText(str(self.feedpertooth))
        self.rev_expr()
        self.feedrate_expr()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = Model()
    mainWindow = MainWindow(model)
    mainWindow.show()
    sys.exit(app.exec_())