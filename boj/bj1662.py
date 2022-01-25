s = input()
stk_len = [0]
stk_mul = list()
for i in range(len(s)):
    c = s[i]
    if c == "(":
        stk_len[-1] -= 1
        stk_len.append(0)
        stk_mul.append(int(s[i-1]))
    elif c == ")":
        tmp = stk_len.pop()*stk_mul.pop()
        stk_len[-1] += tmp
    else:
        stk_len[-1] += 1
print(stk_len[0])
