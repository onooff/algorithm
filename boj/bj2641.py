import sys

input = sys.stdin.readline

n = int(input())
l = list(map(int, input().rstrip().split()))
ok = list()
for _ in range(len(l)):
    ok.append(tuple(l))
    l.append(l.pop(0))
d = {1: 3, 2: 4, 3: 1, 4: 2}
for i in range(len(l)):
    l[i] = d[l[i]]
l.reverse()
for _ in range(len(l)):
    ok.append(tuple(l))
    l.append(l.pop(0))

m = int(input())
ans = list()
for _ in range(m):
    t = tuple(map(int, input().rstrip().split()))
    if t in ok:
        ans.append(t)

print(len(ans))
for t in ans:
    print(*t)
