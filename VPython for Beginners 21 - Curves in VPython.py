from vpython import *
from math import *

list_of_points = []
list_of_points.append(vector(0,0,0))
list_of_points.append(vector(1,1,0))
list_of_points.append(vector(1,0,0))

my_curve = curve(pos = list_of_points)

my_curve.append(vector(0,1,0))
my_curve.append(my_curve.point(0))
my_curve.origin = vector(-0.5,-0.5,-0.5) # origin moved, but camera stil

R = 0.5
dtheta = pi/100
theta = 0
circle_list = []
while theta <= 2*pi:
    circle_list.append(vector(R*cos(theta), R*sin(theta), 0))
    theta += dtheta

print(circle_list)
circle_curve = curve(pos = circle_list)