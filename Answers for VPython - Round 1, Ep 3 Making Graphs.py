from vpython import *

graph(title = "circle", xtitle = "time", ytitle = "position")
x_curve = gcurve(color=color.blue, label="x-coord")
graph(title = "circle", xtitle = "time", ytitle = "position")
y_curve = gcurve(color = color.red, label ="y-coord")

my_sphere = sphere(pos = vector(1,0,0), radius = 0.25, color = vector(0.7,0.52,0.66), make_trail = True, retain = 100, opacity = 0.5)
my_sphere.trail_color = color.cyan

time = 0
dt = 0.01

while time <= 1000:
    rate(100) # Number of frames per second?
    my_sphere.pos.x = cos(time)
    my_sphere.pos.y = sin(time)
    x_curve.plot(time, my_sphere.pos.x)
    y_curve.plot(time, my_sphere.pos.y)
    time = time + dt

print("End of this program.")
