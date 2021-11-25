for _ in range(3):
    s = input()
    last = None
    maxx = 1
    cnt = 1
    for c in s:
        if c == last:
            cnt += 1
        else:
            maxx = max(maxx, cnt)
            cnt = 1
        last = c
    maxx = max(maxx, cnt)
    print(maxx)
