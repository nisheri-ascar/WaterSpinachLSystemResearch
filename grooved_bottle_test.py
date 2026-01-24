from openalea.plantgl.all import *

profile = [
    Vector2(0, 0),        # bottom center
    Vector2(1, 0),        # bottom outer edge
    Vector2(1, 0.5),      # first section
    Vector2(0.9, 0.5),    # groove
    Vector2(1, 1.0),      # next section
    Vector2(0.9, 1.0),
    Vector2(1, 1.5),
    Vector2(0.9, 1.5),
    Vector2(0, 5)         # top center
]

shape = Revolution(profile)
color = Material(Color3(255,0,0))
render = Shape(shape, color)
scene.add(render)
Viewer.display(scene)

