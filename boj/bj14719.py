import sys

input = sys.stdin.readline
input()
l = list(map(int, input().rstrip().split()))

ll = [[0, 0] for _ in range(len(l))]
maxx = -1
for i in range(len(l)):
    if l[i] > maxx:
        maxx = l[i]
    ll[i][0] = maxx

maxx = -1
for i in range(len(l) - 1, -1, -1):
    if l[i] > maxx:
        maxx = l[i]
    ll[i][1] = maxx

ans = 0
for i in range(len(l)):
    minn = min(ll[i])
    if l[i] < minn:
        ans += minn - l[i]
print(ans)
