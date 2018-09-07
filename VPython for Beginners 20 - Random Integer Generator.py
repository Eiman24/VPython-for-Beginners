import random
from math import *

def rand_int(x1, x2):
    r = int(int(x1) + random.random()*(int(x2) - int(x1)))
    return r

for i in range(10):
    print(rand_int(1, 10))