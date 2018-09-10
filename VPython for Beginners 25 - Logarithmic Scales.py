from vpython import *
from math import *

A = 10
b = 0.1

C = 1
p = 2

my_graph = graph(logx = True, logy = True, ymin = 0.1, ymax = 100000)

my_dots_1 = gdots(color = color.red)
my_dots_2 = gdots(color = color.blue)

for i in range(10, 500, 1):
    x = i/10
    rate(1000)
    y = A*exp(b*x)
    my_dots_1.plot(pos = (x,y))
    y = C*x**p
    my_dots_2.plot(pos = (x,y))
