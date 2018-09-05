from vpython import *

sphere_location = vector(0,0,0)
box_location = vector(1,0,0)

sphere(pos = sphere_location, radius = 0.5, color = color.yellow)
box(pos = box_location, size = vector(0.5,0.1,1.0), color = color.red) # size = width, height, depth