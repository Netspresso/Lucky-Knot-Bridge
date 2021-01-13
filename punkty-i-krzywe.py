import apex
from apex.construct import Point3D, Point2D
from apex.geometry import createPointXYZ, createCurve3DNurb
import math
from config import Curve as C
from curves import linspace, Line, Curves_sin
# import numpy as np

apex.setScriptUnitSystem(unitSystemName=r'''m-kg-s-N''')
applicationSettingsGeometry = apex.setting.ApplicationSettingsGeometry()
applicationSettingsGeometry.createGeometryInNewPart = apex.setting.CreateGeometryInNewPart.CurrentPart
applicationSettingsGeometry.geometryTessellationIsWatertight = False
applicationSettingsGeometry.geometryEdgeTesselationTolerance = apex.setting.GeometryTessellationTolerance.Medium
applicationSettingsGeometry.geometryFaceTesselationTolerance = apex.setting.GeometryTessellationTolerance.Medium
apex.setting.setApplicationSettingsGeometry(
    applicationSettingsGeometry=applicationSettingsGeometry)
model_1 = apex.currentModel()
'''Here I began script'''
''' Classes '''

# Lists of points for all Curves
ptList = []
n_of_curve = 24
# count of curves

# Loop which adds empty lists to ptList (now we have list which contain 18 empty lists)
for i in range(0, n_of_curve):
    ptList.append([])

# Generating points
Curves_sin(-5, 150, 5 * math.pi, ptList[0], 2, 3 * math.pi, offsetY=-3)
Curves_sin(-5, 150, 5 * math.pi, ptList[1], -2, 3 * math.pi, offsetY=1)
Curves_sin(-5, 150, 5 * math.pi, ptList[2], 2, 3 * math.pi, offsetY=-1)
Curves_sin(-5, 150, 5 * math.pi, ptList[3], -2, 3 * math.pi, offsetY=3)
Curves_sin(10, 150, 5 * math.pi, ptList[4], -2, 3 * math.pi, offsetY=-1)
Curves_sin(10, 150, 5 * math.pi, ptList[5], 2, 3 * math.pi, offsetY=1)
Curves_sin(10, 150, 5 * math.pi, ptList[6], -2, 3 * math.pi, offsetY=-3)
Curves_sin(10, 150, 5 * math.pi, ptList[7], 2, 3 * math.pi, offsetY=3)
Curves_sin(-5,
           150,
           5 * math.pi,
           ptList[8],
           2,
           3 * math.pi,
           offsetY=-3,
           offsetZ=1.2)
Curves_sin(-5,
           150,
           5 * math.pi,
           ptList[9],
           -2,
           3 * math.pi,
           offsetY=1,
           offsetZ=1.2)
Curves_sin(-5,
           150,
           5 * math.pi,
           ptList[10],
           2,
           3 * math.pi,
           offsetY=-1,
           offsetZ=1.2)
Curves_sin(-5,
           150,
           5 * math.pi,
           ptList[11],
           -2,
           3 * math.pi,
           offsetY=3,
           offsetZ=1.2)
Curves_sin(10,
           150,
           5 * math.pi,
           ptList[12],
           -2,
           3 * math.pi,
           offsetY=-1,
           offsetZ=1.2)
Curves_sin(10,
           150,
           5 * math.pi,
           ptList[13],
           2,
           3 * math.pi,
           offsetY=1,
           offsetZ=1.2)
Curves_sin(10,
           150,
           5 * math.pi,
           ptList[14],
           -2,
           3 * math.pi,
           offsetY=-3,
           offsetZ=1.2)
Curves_sin(10,
           150,
           5 * math.pi,
           ptList[15],
           2,
           3 * math.pi,
           offsetY=3,
           offsetZ=1.2)
Curves_sin(-5.5,
           150,
           5 * math.pi,
           ptList[16],
           2,
           3 * math.pi,
           offsetY=-3,
           offsetZ=-1)
Curves_sin(-5.5,
           150,
           5 * math.pi,
           ptList[17],
           -2,
           3 * math.pi,
           offsetY=1,
           offsetZ=-1)
Curves_sin(-5.5,
           150,
           5 * math.pi,
           ptList[18],
           2,
           3 * math.pi,
           offsetY=-1,
           offsetZ=-1)
Curves_sin(-5.5,
           150,
           5 * math.pi,
           ptList[19],
           -2,
           3 * math.pi,
           offsetY=3,
           offsetZ=-1)
Curves_sin(11,
           150,
           5 * math.pi,
           ptList[20],
           -2,
           3 * math.pi,
           offsetY=-1,
           offsetZ=-2)
Curves_sin(11,
           150,
           5 * math.pi,
           ptList[21],
           2,
           3 * math.pi,
           offsetY=1,
           offsetZ=-2)
Curves_sin(11,
           150,
           5 * math.pi,
           ptList[22],
           -2,
           3 * math.pi,
           offsetY=-3,
           offsetZ=-2)
Curves_sin(11,
           150,
           5 * math.pi,
           ptList[23],
           2,
           3 * math.pi,
           offsetY=3,
           offsetZ=-2)

#  Creating curves through the points
for Curve in range(0, len(ptList)):
    controlPoints = ptList[Curve]  # Lista punktów kontrolnych
    n = len(controlPoints)
    deg = 1  # Stopień krzywej, decyduje o tym, ile punktów kontrolnych wpływa na jej kształt.
    m = n + deg + 1
    knotPoints = linspace(0, 1, m)
    createCurve3DNurb(controlPoints, knotPoints, deg).asCurve()

# beam_ptList = []
# n_of_beams = len(ptList[8])
# for i in range(0, n_of_beams):
#     beam_ptList.append([])

# for i in range(0, n_of_beams):
#     beam_ptList[i].append(ptList[8][i])
#     beam_ptList[i].append(ptList[9][i])

# for beam in range(0, len(beam_ptList)):
#     for point in beam_ptList[beam]:
#         controlPoints = beam_ptList[beam]  # Lista punktów kontrolnych
#         n = len(controlPoints)
#         deg = 1  # Stopień krzywej, decyduje o tym, ile punktów kontrolnych wpływa na jej kształt.
#         m = n + deg + 1
#         knotPoints = linspace(0, 1, m)
#         createCurve3DNurb(controlPoints, knotPoints, deg).asCurve()