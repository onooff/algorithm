t = int(input())

for tc in range(t):
    w, h, p = map(int, input().split())
    cnt = 1
    while w % 2 == 0 or h % 2 == 0:
        if w % 2 == 0:
            w //= 2
            cnt *= 2
        elif h % 2 == 0:
            h //= 2
            cnt *= 2
    if cnt >= p:
        print('YES')
    else:
        print('NO')
