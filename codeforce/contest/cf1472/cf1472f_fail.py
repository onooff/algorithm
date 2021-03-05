import sys


t = int(input())

for tc in range(t):
    input()
    n, m = map(int, input().split())
    black = set()
    for i in range(m):
        black.add(tuple(map(int, input().split())))
    black.add((1, n+1))
    black.add((2, n+1))
    is_ok = True
    for i in range(1, n+1):
        if (1, i) not in black and (2, i) not in black:
            continue
        else:
            if (1, i) not in black:
                if (1, i+1) not in black:
                    black.add((1, i+1))
                else:
                    is_ok = False
                    break
            elif (2, i) not in black:
                if (2, i+1) not in black:
                    black.add((2, i+1))
                else:
                    is_ok = False
                    break
    if is_ok:
        print('YES')
    else:
        print('NO')
