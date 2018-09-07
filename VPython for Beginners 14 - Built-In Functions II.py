from vpython import *
from math import *

graph()
log_graph = gcurve(color = color.red)

def log_a(x,a=exp(1)):
    return log(x)/log(a)

for x in range(1,1000,1):
    log_graph.plot(pos=(x/100, log_a(x/100, 10)))

graph()
stair_graph = gcurve(color = color.red)

for x in range(1,1000,1):
    stair_graph.plot(pos=(x/100, ceil(x/100)))

graph()
fac_graph = gdots(color = color.red)

for x in range(0,10,1):
    fac_graph.plot(pos=(x, factorial(x)))