import math
import apex
from apex.construct import Point3D, Point2D
from apex.geometry import createPointXYZ, createCurve3DNurb


class Curves_sin():
    # Class defining curves A

    def __init__(self,
                 Width,
                 Length,
                 Range,
                 ListPoint,
                 WidthY,
                 RangeY,
                 offsetY=0,
                 offsetZ=0,
                 beginning=0):
        t = beginning
        parametr = Range / Length
        parametrY = RangeY / Length
        while t <= Length:
            self.x = t
            self.y = WidthY * math.sin(parametrY * self.x) + offsetY
            self.z = Width * math.sin(parametr * self.x) + offsetZ
            ListPoint.append(
                createPointXYZ(x=self.x, y=self.y, z=self.z).asPoint())
            t += 0.5


class Line():
    def __init__(self, y, z, begining, Range, ListPoint):
        t = begining
        while t <= Range:
            self.x = t
            self.y = y
            if (t > 0) and (t <= 8):
                self.z = z - t / 8
            elif (t >= 12) and (t < 20):
                self.z = z - 1 + (t - 12) / 8
            else:
                self.z = z

            ListPoint.append(
                createPointXYZ(x=self.x, y=self.y, z=self.z).asPoint())
            t += 0.2


def linspace(low, up, leng):
    """function creating a linear space from [low] to [up] using [leng] number of elements"""
    list = []
    step = (up - low) / float(leng)
    for i in range(leng):
        list.append(low)
        low = low + step
    return list