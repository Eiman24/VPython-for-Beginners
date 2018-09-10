from vpython import *

spring = (helix(pos = vector(0,0,0),
                axis = vector(0,-1,0),
                size = vector(2,0.3,0.3),
                coils = 16,
                stiffness = 1.0))

helix(pos = vector(1,0,0),
      axis = vector(0,-1,0),
      size = vector(1,0.3,0.3),
      coils = 8)

helix(pos = vector(2,0,0),
      axis = vector(0,-1,0),
      size = vector(1,0.3,0.3),
      thickness=0.1)

eq_pos = spring.pos + spring.axis

ball = sphere(pos = spring.pos + spring.axis,
              color = color.red, radius = 0.2,
              mass = 1, velocity = vector(0,1,0),force = vector(0,0,0))

dt = 0.01
while True:
    rate(100)
    ball.force = -spring.stiffness*(ball.pos-eq_pos)
    ball.velocity = ball.velocity + ball.force/ball.mass*dt
    ball.pos = ball.pos + ball.velocity*dt
    spring.axis = ball.pos - spring.pos