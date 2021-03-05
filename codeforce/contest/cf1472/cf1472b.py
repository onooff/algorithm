t = int(input())

for tc in range(t):
    n = int(input())
    candys = list(map(int, input().split()))
    cnt = [0, 0]
    for c in candys:
        if c == 1:
            cnt[0] += 1
        else:
            cnt[1] += 1

    if cnt[0] % 2 == 0 and cnt[1] % 2 == 0:
        print('YES')
    elif cnt[0] % 2 == 1:
        print('NO')
    elif cnt[0] == 0:
        print('NO')
    else:
        print('YES')
