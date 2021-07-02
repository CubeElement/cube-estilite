import math


class Model():
    def __init__(self):
        self.datatable = self.create_cuttingdata()

    def speed_formula(self, revolutions, diameter):
        speed = (math.pi * diameter * revolutions) / 1000
        return round(speed, 100)

    def revolutions_formula(self, cutting_speed, diameter):
        revolutions = (cutting_speed * 1000) / (math.pi * diameter)
        return round(revolutions, 100)

    def feedrate_formula(self, speed, znum, feedpertooth):
        feedrate = speed * feedpertooth * znum
        return round(feedrate, 100)

    def feedpertooth_formula(self, speed, znum, feedrate):
        feedpertooth = feedrate / (speed * znum)
        return round(feedpertooth, 100)

    def create_cuttingdata(self):
        standard_cutting_parameters = {"P": [80, 0.03],
                                       "M": [50, 0.025],
                                       "K": [100, 0.05],
                                       "N": [250, 0.07],
                                       "S": [70, 0.04],
                                       "H": [35, 0.02]}
        return standard_cutting_parameters
