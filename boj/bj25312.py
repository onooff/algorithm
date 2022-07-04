import math
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
juices = list()
for i in range(n):
    w, v = map(int, input().split())
    juices.append((-v/w, w, v))
juices.sort()

ans = 0
d = 1
idx = 0
while m > 0:
    cur = juices[idx]
    idx += 1
    if cur[1] > m:
        d = cur[1]
        ans *= d
        ans += cur[2]*m
        m = 0
    else:
        ans += cur[2]
        m -= cur[1]
GCD = math.gcd(d, ans)
print(ans//GCD, '/', d//GCD, sep='')
