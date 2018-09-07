from vpython import *

text = "text is"
print(text +" good")

a = 2*2/4*6
a = str(a)
text2 = "hahahhah " + a
print(text2)

my_sphere = sphere(pos = vector(1,0,0), radius = 0.1, color = color.red)
label(pos = vector(0,0,0))

dt = 0.01
for i in range(0,1000):
    rate(100)
    my_sphere.pos.x += dt
    label(pos=vector(0, 0, 0),text = "The ball is at {:.1f}".format(my_sphere.pos.x))