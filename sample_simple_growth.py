# basic geometric grow, just for self testing purposes

from openalea.plantgl.all import *

length = 1.0

for step in range(10):
    length += 0.5 

    stem = Cylinder(radius=0.1, height=length)
    shape = Shape(stem, Material(Color3(0, 200, 0)))

    scene = Scene([shape])
    Viewer.display(scene)
