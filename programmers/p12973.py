def solution(s):
    if len(s) % 2 == 1:
        return 0

    stk = list()
    for i in range(len(s)):
        c = s[i]
        if len(stk) > 0 and stk[len(stk)-1] == c:
            stk.pop()
        else:
            stk.append(c)
    if len(stk) == 0:
        return 1
    else:
        return 0
