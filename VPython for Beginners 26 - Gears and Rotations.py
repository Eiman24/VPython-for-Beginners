from vpython import *
from math import *

g1 = shapes.gear(n = 20)
gear_1 = extrusion(path=[vector(0,0,0), vector(0,0,0.1)], shape = g1)

g2 = shapes.gear(n = 10, radius = 0.5)
gear_2 = extrusion(path=[vector(1.5,0,0), vector(1.5,0,0.1)], shape = g2)
gear_2.rotate(axis = vector(0,0,1), angle = 2*pi/20)

dt = 0.01
omega = 0.5

while True:
    rate(100)
    gear_1.rotate(axis = vector(0, 0, 1), angle = omega*dt)
    gear_2.rotate(axis = vector(0, 0, 1), angle = -2*omega * dt)
