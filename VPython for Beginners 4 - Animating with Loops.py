from vpython import *

my_sphere = sphere(pos = vector(0,0,0), radius = 0.25, color = color.green)

i = 1

while i <= 5:
    rate(1) # Number of frames per second?
    my_sphere.pos.x = my_sphere.pos.x + 1
    i = i + 1

print("End of this program.")


