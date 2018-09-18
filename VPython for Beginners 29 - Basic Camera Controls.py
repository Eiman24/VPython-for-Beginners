from vpython import *
from math import *

box(pos = vector(10,10,10), color = color.red)
box(pos = vector(-10,10,10), color = color.blue)
box(pos = vector(10,-10,10), color = color.green)
box(pos = vector(-10,-10,10), color = color.white)
box(pos = vector(10,10,-10), color = color.orange)
box(pos = vector(-10,10,-10), color = color.cyan)
box(pos = vector(10,-10,-10), color = color.magenta)
box(pos = vector(-10,-10,-10), color = color.yellow)

print(scene.camera.pos)
print(scene.camera.axis)

ball = sphere(pos = vector(10, 0 ,0))
scene.camera.follow(ball)

dtheta = 0.05
theta = 0
while True:
    rate(20)
    ball.pos = vector(10*cos(theta), 10*sin(theta), 0)
    theta += dtheta