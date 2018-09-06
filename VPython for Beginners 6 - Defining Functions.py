from math import *

# Pythagorean Theorem
def pt(side1=3, side2=4):
    hyp = sqrt(side1**2 + side2**2)
    return hyp

print(pt())
print(pt(3, 4))
print(pt(5, 12))
print(pt(2,2))

# Factorial Function
def factorial(n):
    if (n%1 != 0) or (n < 0):
        raise ValueError("The value is Negative or not an Integer")
    elif n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(0))
print(factorial(3))
print(factorial(-5))