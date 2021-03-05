import math
t = int(input())

for tc in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    c = [0, 0, 0]

    for num in a:
        c[num % 3] += 1

    chk = n//3
    ans = 0
    for i in range(3):
        if c[i] > chk:
            ans += c[i]-chk
            c[(i+1) % 3] += c[i]-chk
            c[i] = chk
    for i in range(3):
        if c[i] > chk:
            ans += c[i]-chk
            c[(i+1) % 3] += c[i]-chk
            c[i] = chk
    print(ans)
