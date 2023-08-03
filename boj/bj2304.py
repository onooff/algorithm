import sys

input = sys.stdin.readline

n = int(input())
maxx = (0, 0)
l = list()
for _ in range(n):
    p = tuple(map(int, input().split()))
    if p[1] > maxx[1]:
        maxx = p
    l.append(p)
l.sort(key=lambda x: x[0])


ans = 0
h = 0
for i in range(len(l)):
    if l[i] == maxx:
        break
    if l[i][1] > h:
        h = l[i][1]
    ans += h * (l[i + 1][0] - l[i][0])
h = 0
for i in range(len(l) - 1, -1, -1):
    if l[i] == maxx:
        break
    if l[i][1] > h:
        h = l[i][1]
    ans += h * (l[i][0] - l[i - 1][0])
ans += maxx[1]

print(ans)
