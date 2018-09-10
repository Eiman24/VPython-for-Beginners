from vpython import *

cylinder(pos = vector(0,0,0),
         axis = vector(1,0,0),
         size = vector(1,0.1,0.1),
         color = color.white,
         opacity = 1)
cylinder(pos = vector(0,0,0),
         axis = vector(0,1,0),
         size = vector(1,0.1,0.1),
         color = color.white,
         opacity = 1)
cylinder(pos = vector(0,0,0),
         axis = vector(0,0,1),
         size = vector(1,0.1,0.1),
         color = color.white,
         opacity = 1)
# scene.camera.pos = vector(1,1,0)

cone(pos = vector(2,0,0),
         axis = vector(0,1,0),
         size = vector(1,0.5,0.5),
         color = color.yellow,
         opacity = 1)