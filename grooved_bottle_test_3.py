from openalea.plantgl.all import *

# ------------------------
# 1️⃣ Define the bottle profile (radius vs height)
# ------------------------
profile = Polyline2D([
    (1.2, 0.0),   # bottom outer radius
    (1.2, 5.0),   # straight body
    (0.9, 6.0),   # shoulder
    (0.9, 7.0),   # neck
])

# ------------------------
# 2️⃣ Create full circular bottle using Revolution
# ------------------------
full_bottle = Revolution(profile, slices=64)  # smoother circle

# ------------------------
# 3️⃣ Define cutting box for open side
# ------------------------
# The box should cover the side you want to remove
cut_box = Box(3.0, 10.0, 10.0)  # big enough to remove one vertical slice
cut_box = Translated(Vector3(0.0, 0.0, 0.0), cut_box)  # move it in front of the bottle

# You can rotate the box to adjust where the opening is
cut_box = EulerRotated(Vector3(0, 0, 0.0), Vector3(0,0, 0.0), cut_box)  # rotate if needed

# ------------------------
# 4️⃣ Subtract the box from the bottle
# ------------------------
bottle_with_open_side = CSGDifference(full_bottle, cut_box)

# ------------------------
# 5️⃣ Assign material (plastic bottle look)
# ------------------------
bottle_material = Material(
    Color3(120, 180, 255),  # light blue
    transparency=0.3
)

bottle_shape = Shape(bottle_with_open_side, bottle_material)

# ------------------------
# 6️⃣ Display
# ------------------------
scene = Scene([bottle_shape])
Viewer.display(scene)

