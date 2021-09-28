import sys
import math

mod = 1000000007


def calc(n, d):
    global mod
    if d == 0:
        return 1

    res = calc(n, d//2) % mod
    if d % 2 == 0:
        return res * res % mod

    return (res * res % mod * n % mod) % mod


inputs = sys.stdin.readlines()

m = int(inputs[0])
ans = 0

for i in range(1, m+1):
    n, s = map(int, inputs[i].rstrip().split())
    gcd = math.gcd(n, s)
    n, s = n//gcd, s//gcd
    a = calc(n, mod-2)
    b = (a*s) % mod
    ans += b

print(ans % mod)
