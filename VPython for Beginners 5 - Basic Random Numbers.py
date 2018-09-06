from random import *
from math import *

for i in range(0, 20):
    print(random())

a = 90
b = 100
for i in range(0, 20):
    # generate a random number between a & b
    print(a + random()*(b-a))

print("--------------------------")

def uniform(a=1, b=100):
    r = a + random()*(b-a)
    return r

print(uniform())
print(uniform(pi, 2*pi))
print(uniform(-10, -20))
print(uniform(-5, 5))