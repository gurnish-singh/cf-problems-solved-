from fractions import gcd
from math import sqrt
def countFactors(n):
    s = int(sqrt(n))
    c = 0
    for i in range(1, s+1):
        if (n % i == 0):
            if i != n/i: c += 2
            else: c += 1
    return c
 
n, data = int(input()), [int(i) for i in input().strip().split()]
g = data[0]
for i in range(1, n): g = gcd(g, data[i])
print(countFactors(g))
