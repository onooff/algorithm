l = list(map(int, input().split()))
l.sort()

ans = l[2]
while True:
    cnt = 0
    for d in l:
        if ans < d:
            break
        if ans % d == 0:
            cnt += 1
            if cnt >= 3:
                break
    if cnt >= 3:
        break

    ans += 1

print(ans)
