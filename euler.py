from math import sqrt


def F(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))


n = 40
fib40 = F(n)
print(F(n))

