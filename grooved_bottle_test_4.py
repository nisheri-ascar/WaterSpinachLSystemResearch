
print("this one works!")
from openalea.plantgl.all import *

scene = Scene()
# Bottle parameters

def bottle():
    # Physical Attributes
    global scene 
    height = 2
    num_slices = 4
    radius = 3
    groove_depth = 0.1
    # Visual Attributes
    ambient = Color3(0,0,255)
    diffuse = 1.0
    specular = Color3(0,0,0)
    emmision = Color3(0,0,0) # wat the fuck is this again?
    shininess = 0.2
    transparency = 1
    for i in range(num_slices):
        # Alternate radius to make groove_depth
        
        r = radius - (groove_depth if i % 2 else 0)
        z = i * (height / num_slices)
        print(f"iteration: {i}")
        print(f"r = {r}")
        print(f"z = {z}")
        slice_cyl = Translated(0, 0, z, Cylinder(r, height / num_slices, 1))
        scene += Shape(slice_cyl, Material(ambient, diffuse, specular, emmision, shininess, transparency))
bottle()
Viewer.display(scene)

