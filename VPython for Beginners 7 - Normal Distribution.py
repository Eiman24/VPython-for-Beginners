from random import *
from math import *

# Normal Distribution 正态分布
def normal(avg, stdev):
    u1 = random()
    u2 = random()
    r = sqrt(-2*log(u1)) * cos(2*pi*u2)
    r = r*stdev + avg
    return r

print(normal(5,0.1))