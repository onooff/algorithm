s = input()
while s != '.':
    sl = len(s)
    ans = 1
    for i in range(1, sl):
        if sl % i == 0:
            chk = s[:i]
            is_ans = True
            for j in range(i, sl, i):
                if s[j:j+i] != chk:
                    is_ans = False
                    break
            if is_ans:
                ans = sl//i
                break
    print(ans)
    s = input()
