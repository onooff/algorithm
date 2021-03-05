import math
t = int(input())

for tc in range(t):
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    i = 0
    ans = 0
    while i < len(l) and l[i] % x == 0:
        ans += l[i]
        new = l[i]//x
        for j in range(x):
            l.append(new)
        i += 1
        # print(i, l[i], i < len(l), l[i] % x == 0)
    while i < len(l):
        ans += l[i]
        i += 1
    print(ans)
