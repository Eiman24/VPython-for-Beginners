from vpython import *
from math import *

circle = shapes.circle()
box = shapes.circle()

circle_path = [vector(0,0,0), vector(0,0,0.1)]

disc = extrusion(path = circle_path, shape = circle)

disc.color = color.yellow
disc.pos = vector(1,1,0)

ej_path = [vector(0,0,2), vector(0,0,3), vector(1,0,3)]

ej = extrusion(path = ej_path, shape = circle)

circular_path = []
theta = 0
while(theta <= 2*pi*1.01):
    circular_path.append(vector(cos(theta), 0, sin(theta)))
    theta += 2*pi/100
donut = extrusion(path = circular_path, shape = box)