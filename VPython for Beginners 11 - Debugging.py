from vpython import *
from math import  *

xmin = -2*pi
xmax = 2*pi
dx = 0.01

cube = box(size = vector(0.2,0.2,0.2), pos = vector(xmin,0,0), color = color.red, make_trail = True)

while cube.pos.x < xmax:
    rate(100)
    cube.pos.x = cube.pos.x + dx
    cube.pos.y = sin(cube.pos.x)
