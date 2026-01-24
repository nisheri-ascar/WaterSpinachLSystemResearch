from openalea.plantgl.all import *

# Water bottle
profile = Polyline2D([
    (0.0, 0.0),
    (1.2, 0.0),
    (1.2, 5.0),
    (0.9, 6.0),
    (0.9, 7.0),
])

path = Polyline([
    (1.0, 0.0, 0.0),
    (0.7, 0.7, 0.0),
    (0.0, 1.0, 0.0),
])

quarter_bottle = Extrusion(path, profile)

shape = Shape(
    quarter_bottle,
    Material(Color3(120, 180, 255), transparency=0.2)
)

Viewer.display(Scene([shape]))


