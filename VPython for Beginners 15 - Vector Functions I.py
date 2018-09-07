from vpython import *
from math import *

a = vector(3,4,0)
print(mag(a))

ahat = a.hat # Unit Vector
print(ahat)
print(mag(ahat))

b = vector(0,2,1)
print(a+b)
print(a-b)

print(dot(a,b)) # Dot product
print(cross(a,b))