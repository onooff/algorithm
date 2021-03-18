t = int(input())

for tc in range(t):
    s = list(input())
    s = list(map(int, s))
    s.insert(0, -1)
    chk = [True for i in range(len(s))]
    ans = 'yes'
    now = 0
    for i in range(1, len(s)):
        if s[i] == now:
            continue
        else:
            if chk[i-1]:
                chk[i] = False
            else:
                now += 1
                if now > 1:
                    ans = 'no'
                    break
    print(ans)
