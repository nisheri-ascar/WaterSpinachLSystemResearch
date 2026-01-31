print("pro tip: sleep is optional")
from openalea.plantgl.all import *
import math
import random

# Global Tweakable Options
scene = Scene()
circle_slices = 64
radius = 3
groove_depth = 0.2
height = 2

def bottle():
    global scene 
    global circle_slices

    # -------------------------
    # Tweakable parameters
    # -------------------------
    global height
    num_slices = 10
    global radius
    global groove_depth
    transition_ratio = 0.3    # how tall the downslope is
    num_pts_slope = 10        # smoothness of the curve

    # -------------------------
    # Visual Attributes
    # -------------------------
    ambient = Color3(128,128,128)
    diffuse = 1.0
    specular = Color3(0,0,0)
    emmision = Color3(0,0,0)
    shininess = 0.2
    transparency = 0.1

    material = Material(ambient, diffuse, specular, emmision, shininess, transparency)

    # -------------------------
    # Slice + slope parameters
    # -------------------------
    slice_h = height / num_slices
    transition_h = slice_h * transition_ratio
    body_h = slice_h - transition_h

    # -------------------------
    # Build cylinder slices with curved downslope
    # -------------------------
    for i in range(num_slices):
        r0 = radius - (groove_depth if i % 2 else 0)
        r1 = radius - (groove_depth if (i + 1) % 2 else 0)
        z = i * slice_h
        is_last = (i == num_slices - 1)

        print(f"iteration: {i}, r0={r0}, r1={r1}, z={z}")

        # --- main cylinder ---
        cyl_h = slice_h
        slice_cyl = Translated(
            0, 0, z,
            Cylinder(r0, cyl_h, 0, circle_slices)  # use circle_slices here
        )
        scene += Shape(slice_cyl, material)

        # --- curved polyline slope for groove ---
        if not is_last and r0 != r1:
            pts = []
            for j in range(num_pts_slope + 1):
                t = j / num_pts_slope
                # cosine easing for smooth slope
                eased_t = (1 - math.cos(math.pi * t)) / 2
                radius_at_t = r0 + eased_t * (r1 - r0)
                height_at_t = z + body_h + eased_t * transition_h
                pts.append(Vector2(radius_at_t, height_at_t))
            slope_polyline = Polyline2D(pts)
            slope_revolved = Revolution(slope_polyline, slices=circle_slices)  # use circle_slices
            scene += Shape(slope_revolved, material)

    # -------------------------
    # Bottom cap
    # -------------------------
    scene += Shape(Cylinder(radius, 0.001, 1, circle_slices), material)

def soil():
    global scene
    global circle_slices
    wall_thickness = 0.15
    soil_radius = radius - groove_depth - wall_thickness
    soil_height = height * 0.6
    soil_z = 0.001 # sane number for the cap i think

    soil_material = Material(
            Color3(110, 70, 40), #TODO: use actual soil texture
            1.0,
            Color3(0,0,0),
            Color3(0,0,0),
            0.05,
            0.0 # AGAIN?!?! FUCK YOU ITS 0.0 

            )
    soil = Translated(
            0,0, soil_z,
            Cylinder(
                soil_radius,
                soil_height,
                1,
                circle_slices
                )
            )
    scene += Shape(soil, soil_material)

def kangkong_stem(scene, start_position=(0, 0, 0), num_segments=5, segment_length=3, 
                  base_radius=0.2, taper_factor=0.8, curvature=0.3, material=None):
    """
    Creates a kangkong stem with hollow, segmented structure.
    
    Parameters:
    - scene: The PlantGL scene to add the stem to
    - start_position: (x, y, z) starting position of the stem
    - num_segments: Number of stem segments (internodes)
    - segment_length: Length of each segment
    - base_radius: Radius at the base of the stem
    - taper_factor: How much the stem tapers (0.7-0.9 typical)
    - curvature: How much the stem curves (0=straight, higher=more curved)
    - material: Stem material (if None, creates default green material)
    """
    
    if material is None:
        material = Material(
            Color3(80, 120, 70),  # Stem green color
            0.8,  # diffuse
            Color3(30, 40, 20),  # specular
            Color3(0, 0, 0),  # emission
            0.1,  # shininess
            0.0   # transparency
        )
    
    node_material = Material(
        Color3(100, 140, 90),  # Slightly different color for nodes
        0.9,
        Color3(30, 40, 20),
        Color3(0, 0, 0),
        0.2,
        0.0
    )
    
    x, y, z = start_position
    current_position = Vector3(x, y, z)
    
    # Create a polyline for the stem center
    points = [current_position]
    
    # Create each segment
    for i in range(num_segments):
        # Calculate current radius with taper
        current_radius = base_radius * (taper_factor ** i)
        
        # Add some natural curvature - kangkong stems often curve slightly
        angle_variation = curvature * (random.random() - 0.5)
        
        # Calculate end position for this segment
        end_x = x + math.cos(i * 0.5 + angle_variation) * segment_length * 0.2
        end_y = y + math.sin(i * 0.5 + angle_variation) * segment_length * 0.2
        end_z = z + (i + 1) * segment_length
        
        end_position = Vector3(end_x, end_y, end_z)
        points.append(end_position)
        
        # Create hollow cylinder segment (stem internode)
        # Outer cylinder
        outer_cylinder = Cylinder(
            current_radius,
            segment_length,
            solid=False  # Important: hollow stem!
        )
        
        # Inner hollow part (slightly smaller radius)
        inner_radius = current_radius * 0.7
        inner_cylinder = Cylinder(
            inner_radius,
            segment_length * 1.05,  # Slightly longer to ensure overlap
            solid=False
        )
        
        # Position the segment
        segment_group = Group()
        
        # Calculate direction vector for this segment
        if i == 0:
            direction = Vector3(0, 0, 1)
        else:
            direction = (end_position - points[i]).normalize()
        
        # Create transformation for the segment
        # Kangkong stems often have a slight tilt
        tilt_angle = math.radians(5 * (random.random() - 0.5))
        
        # Create segment with orientation
        segment_transform = Oriented(
            direction,
            Translated(
                current_position,
                Scaled(
                    (1, 1, 1),
                    outer_cylinder
                )
            )
        )
        
        inner_transform = Oriented(
            direction,
            Translated(
                current_position,
                Scaled(
                    (inner_radius/current_radius, inner_radius/current_radius, 1.05),
                    outer_cylinder  # Reusing outer shape with different scale
                )
            )
        )
        
        # Add to scene
        scene += Shape(segment_transform, material)
        scene += Shape(inner_transform, Material(
            Color3(60, 90, 50),
            0.7,
            Color3(20, 30, 15),
            Color3(0, 0, 0),
            0.05,
            0.3  # Slight transparency for inner part
        ))
        
        # Add node (slightly swollen at joints)
        node_radius = current_radius * 1.2
        node = Sphere(node_radius, slices=16, stacks=8)
        node_transform = Translated(current_position, node)
        scene += Shape(node_transform, node_material)
        
        # Update position for next segment
        current_position = end_position
        x, y, z = end_x, end_y, end_z
    
    # Add final node at tip
    final_node = Sphere(base_radius * 0.8, slices=16, stacks=8)
    final_node_transform = Translated(current_position, final_node)
    scene += Shape(final_node_transform, node_material)
    
    # Create the central polyline (for visualization of stem path)
    polyline_3d = Polyline(points)
    scene += Shape(polyline_3d, Material(Color3(255, 0, 0), 1, Color3(0, 0, 0), Color3(0, 0, 0), 1, 0.5))
    
    return current_position  # Return tip position for adding leaves later

# order matters..
soil()
bottle()
kangkong_stem(scene)
Viewer.display(scene)

