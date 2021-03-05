import math
t = int(input())

for tc in range(t):
    n, k = map(int, input().split())
    nk = k
    while n > nk:
        nk += k
    nn = n
    ans = 1
    # while nk > nn:
    #     ans += 1
    #     nn += n
    # print(ans)
    print(math.ceil(nk/n))
    pass
