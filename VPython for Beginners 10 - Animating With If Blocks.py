from vpython import *

my_sphere = sphere(pos = vector(0,0,0), radius = 0.25, color = color.green)
wall_R = box(pos = vector(2,0,0), size = vector(0.1,1,1), color = color.white)
wall_L = box(pos = vector(-2,0,0), size = vector(0.1,1,1), color = color.white)

i = 1
dir = 0.01
# while i <= 1000:
#     rate(100)
#     my_sphere.pos.x = my_sphere.pos.x + 2*dir
#     if my_sphere.pos.x >= (2-0.1/2-my_sphere.radius) and dir > 0:
#         dir = -dir
#     elif my_sphere.pos.x <= (-(2-0.1/2-my_sphere.radius)) and dir < 0:
#         dir = -dir
while i <= 1000:
    rate(100)
    my_sphere.pos.x = my_sphere.pos.x + 2*dir
    if my_sphere.pos.x >= (2-0.1/2-my_sphere.radius) or my_sphere.pos.x <= (-(2-0.1/2-my_sphere.radius)):
        dir = -dir

print("End of this program.")
