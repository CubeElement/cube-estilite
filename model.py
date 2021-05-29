from PyQt5 import QtWidgets


class Model():
    def __init__(self):
        self.datatable = self.create_cuttingdata()

    def speed_formel(self, revolutions, diameter):
        speed = (3.14*float(diameter)*float(revolutions))/1000
        return ("{:.0f}".format(round(float(speed), 0)))

    def revolutions_formel(self, cutting_speed, diameter):
        revolutions = (float(cutting_speed)*1000)/(3.14*float(diameter))
        return ("{:.0f}".format(round(float(revolutions), 0)))

    def feedrate_formel(self, speed, feedpertooth, znum):
        feedrate = float(speed)*float(feedpertooth)*float(znum)
        return ("{:.0f}".format(round(float(feedrate), 0)))

    def feedpertooth_formel(self, speed, feedrate, znum):
        feedpertooth = float(feedrate)/(float(speed)*float(znum))
        return ("{:.3f}".format(round(float(feedpertooth), 3)))

    def create_cuttingdata(self):
        standard_cutting_parameters = {"P":[80, 0.03],
                              "M":[50, 0.025],
                              "K":[100, 0.05],
                              "N":[250, 0.07],
                              "S":[70, 0.04],
                              "H":[35, 0.02]
        }
        return standard_cutting_parameters
