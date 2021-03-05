t = int(input())

for tc in range(t):
    a, b = map(int, input().split())
    l = 0
    r = 0
    aTurn = True
    while a > 0 and b > 0:
        a -= 1
        b -= 1
        if aTurn:
            if a > 0 and b == 0:
                a -= 1
                l += 1
            else:
                r += 1
        else:
            if b > 0 and a == 0:
                b -= 1
                r += 1
            else:
                l += 1
        aTurn = not aTurn
    l += a
    r += b
    print(l, r)
