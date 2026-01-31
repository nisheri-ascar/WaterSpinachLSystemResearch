from openalea.plantgl.all import *

def kangkong_stem():
    t = PglTurtle()
    t.setWidth(0.02)
    #t.setMaterial(Material(Color3(110, 180, 110)))

    # Grow straight up first
    t.forward(1.0)

    # Gentle curve (like your photo)
    for i in range(8):
        t.turn(6)      # slight bend
        t.forward(0.4)

    return getScene()

Viewer.display(kangkong_stem())

