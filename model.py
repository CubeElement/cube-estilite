from PyQt5 import QtWidgets


class Model():
    def __init__(self):
        pass



    def speed_formel(self, revolutions: float, diameter: float):
        speed = (3.14*diameter*revolutions)/1000
        return ("{:.0f}".format(round(float(speed), 0)))

    def revolutions_formel(self, cutting_speed: float, diameter: float):
        revolutions = (cutting_speed*1000)/(3.14*diameter)
        return ("{:.0f}".format(round(float(revolutions), 0)))

    def feedrate_formel(self, feedpertooth):
        pass

    def feedpertooth_formel(self, feedrate):
        pass
    
