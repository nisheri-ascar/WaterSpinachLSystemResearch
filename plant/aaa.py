from openalea.plantgl.all import *

def kangkong_stem():
    turtle = PglTurtle()
    turtle.setWidth(0.02)
    turtle.setColor(Color3(110, 180, 110))

    # Start upright
    turtle.pitch(90)

    # Lower straight part
    turtle.forward(1.0)

    # Gentle natural curve (like your photo)
    for i in range(6):
        turtle.pitch(-5)     # slight bend forward
        turtle.forward(0.5)

    return turtle.getScene()

Viewer.display(kangkong_stem())

