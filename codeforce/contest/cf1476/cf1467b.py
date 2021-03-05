import math
t = int(input())

for tc in range(t):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    s = sum(l)
    chk = k/100
    d = 100/k
    ans = 0
    for i in range(n-1, 0, -1):
        s -= l[i]
        if l[i]/s > chk:
            ns = math.ceil((l[i]*100)/k)
            ans += ns-s
            # print(ns, s)
            s = ns
    print(ans)
