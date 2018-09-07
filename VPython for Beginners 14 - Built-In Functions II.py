from vpython import *
from math import *

fun_graph = gcurve(color = color.red)

def sec(x):
    return 1/cos(x)

for x in range(-1000,1000,1):
    fun_graph.plot(pos=(x/100, sec(x/100)))