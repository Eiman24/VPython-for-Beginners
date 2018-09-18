from vpython import *

box1 = box(pos = vector(-1,0,0), size = vector(0.1,2,0.1), color = color.green)
box2 = box1.clone(pos = vector(1,0,0), color = color.blue)

boxes = compound([box1, box2])

c1 = cylinder(pos = vector(0,0,0), axis = vector(1,0,0), radius = 0.05)
c2 = c1.clone(axis = vector(0,1,0))
c3 = c1.clone(axis = vector(-1,0,0))
c4 = c1.clone(axis = vector(0,-1,0))

pinwheel = compound([c1,c2,c3,c4], pos = vector(0,-2,0))

for i in range(1000):
    rate(30)
    boxes.pos += vector(0.01,0,0)
    pinwheel.rotate(axis = vector(0,0,1), angle = 0.1)