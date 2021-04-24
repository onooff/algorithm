def solution(dirs):
    chk = set()
    y = 0
    x = 0
    last = (0, 0)
    ans = 0
    for c in dirs:
        if c == 'U':
            if y + 1 > 5:
                continue
            y += 1
        elif c == 'D':
            if y - 1 < -5:
                continue
            y -= 1
        elif c == 'L':
            if x - 1 < -5:
                continue
            x -= 1
        elif c == 'R':
            if x + 1 > 5:
                continue
            x += 1
        now = (y, x)
        go = (last, now)
        chk.add(go)
        go = (now, last)
        chk.add(go)
        last = now
    print(chk)
    return len(chk) // 2
