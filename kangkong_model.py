from openalea.plantgl.all import *

IMAGE_OUTPUT=""

def model_bottlepot():
    scene = Scene()

    # Physical properties
    radius = 0.4
    height = 0.5
    # Color properties
    ambient = Color3(255,0,0)
    diffuse = 1.0
    specular = Color3(0,0,0)
    bottlePot_Opacity = 1.0
    #bottlePot_WholeColor = Material(bottlePot_ColorFirst, bottlePot_ColorSecond, bottlePot_ColorThird, bottlePot_Opacity, 0)
    # Self note: Material(ambient, diffuse, specular, opacity and something..?)
    shape = Cylinder(radius, height, caps)
    bottlePot_WholeColor = Material(Color3(255,0,0))
    
    bottlePot_RenderableObject = Shape(bottlePot_Shape, bottlePot_WholeColor)

    scene.add(bottlePot_RenderableObject)
    Viewer.display(scene)

"""
def Model_BottlePot():
    outer = Cylinder(1.0, 5.0)
    inner = Translated(0, 0, 0.1, Cylinder(0.9, 4.8))
    print(outer)
    
    print(inner)

    pot = TaperedCylinder(1.0, 0.9, 5.0)

    pot_material = Material(
        diffuse=Color3(200, 50, 50),
        transparency=0.3
    )

    scene = Scene([Shape(pot_geometry, pot_material)])
    Viewer.display(scene)
"""

def Model_Soil():
    pass

def Model_Stem():
    pass

def Model_Leafs():
    pass

def main():
    model_bottlepot()

# Self note: there is technically no need for while true loop since this file is technically just a script for PlantGL
main()
