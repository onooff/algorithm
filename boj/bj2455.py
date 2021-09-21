n = 0
maxx = 0
for _ in range(4):
    out, come = map(int, input().split())
    n -= out
    n = min(10000, n+come)
    maxx = max(maxx, n)
print(maxx)
