a = 10
b = 3

print(a, "/", b, "=", a/b)

print(int(a/b))
print(10%3)

def is_prime(n):
    if n == int(n) and n > 1:
        for i in range(2,n):
            if(n%i == 0):
                print("not a prime number")
                return False
        print("is a prime number")
        return True
    print("not a integer number greater than 1")
    return False

is_prime(0)
is_prime(12)
is_prime(17)
is_prime(18)
is_prime(18.5)
is_prime(71)
is_prime(1)
