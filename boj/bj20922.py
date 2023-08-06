import sys

input = sys.stdin.readline
n, k = map(int, input().rstrip().split())
l = list(map(int, input().rstrip().split()))

tail = -1
d = dict()
maxx = 0
for i in range(n):
    d.setdefault(l[i], 0)
    d[l[i]] += 1
    while d[l[i]] > k:
        tail += 1
        d[l[tail]] -= 1
    maxx = max(maxx, i - tail)

print(maxx)
