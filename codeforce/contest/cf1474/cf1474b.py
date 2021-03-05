import math

t = int(input())
for tc in range(t):
    d = int(input())
    if d > 1 and (1+d) % 2 == 0:
        d += 1
    a = 1+d
    b = 1+d+d
    gcd = math.gcd(a, b)
    print(
        (a//gcd)*(b//gcd)
    )
