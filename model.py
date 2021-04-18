from PyQt5 import QtWidgets


class Model():
    def __init__(self):
        pass



    def speed_formel(self, revolutions, diameter):
        speed = (3.14*float(diameter)*float(revolutions))/1000
        return ("{:.0f}".format(round(float(speed), 0)))

    def revolutions_formel(self, cutting_speed, diameter):
        revolutions = (float(cutting_speed)*1000)/(3.14*float(diameter))
        return ("{:.0f}".format(round(float(revolutions), 0)))

    def feedrate_formel(self, speed, feedpertooth, znum):
        print("speed f z", speed, feedpertooth, znum)
        feedrate = float(speed)*float(feedpertooth)*float(znum)
        return ("{:.0f}".format(round(float(feedrate), 0)))

    def feedpertooth_formel(self, speed, feedrate, znum):
        feedpertooth = float(feedrate)/(float(speed)*float(znum))
        return ("{:.3f}".format(round(float(feedpertooth), 3)))
