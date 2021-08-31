t = int(input())
for tc in range(t):
    n = int(input())
    d = dict()
    ok = True
    for i in range(n):
        s = input()
        if not ok:
            continue
        cur = d
        for i in range(len(s)):
            c = s[i]
            if i == len(s)-1:
                if c in cur:
                    ok = False
                    break
                cur.setdefault(c, -1)
            else:
                chk = cur.setdefault(c, dict())
                if chk == -1:
                    ok = False
                    break
                cur = cur[c]
    if ok:
        print('YES')
    else:
        print('NO')
