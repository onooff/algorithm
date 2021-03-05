import math
t = int(input())

for tc in range(t):
    i = int(input())
    l = list(map(int, input().split()))

    ans = 0
    idx = 0
    while True:
        chk = max(l[idx], l[idx+1])/min(l[idx], l[idx+1])
        if chk > 2:
            if l[idx] > l[idx+1]:
                l.insert(idx+1, math.ceil(l[idx]/2))
            else:
                l.insert(idx+1, math.ceil(l[idx+1]/2))
            ans += 1
        else:
            idx += 1
            if idx == len(l)-1:
                break
    # print(">>>", ans, l)
    print(ans)
