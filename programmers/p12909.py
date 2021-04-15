def solution(s):
    stk = list()
    for i in range(len(s)):
        c = s[i]
        if c == ')':
            if len(stk) == 0 or stk[-1] != '(':
                return False
            else:
                stk.pop()
        else:
            stk.append(c)
    if len(stk) == 0:
        return True
    else:
        return False
