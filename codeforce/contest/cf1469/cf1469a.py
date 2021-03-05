t = int(input())

for tc in range(t):
    stk = list()
    s = input()
    is_OK = True

    if len(s) % 2 == 1 or s[0] == ')' or s[len(s)-1] == '(':
        print('NO')
        continue

    cnt = 0
    cntq = 0

    for c in list(s):
        if c == '(':
            cnt += 1
        elif c == ')':
            cnt -= 1
        else:  # c=='?'
            cntq += 1

    cnt = abs(cnt)
    # print('>>>', cnt, cntq)
    if cnt == 0 and cntq % 2 == 0:
        print('YES')
    else:
        if cnt == cntq:
            print('YES')
        else:
            print('NO')

    # for c in list(s):
    #     if c == '?':
    #         if len(stk) != 0 and stk[len(stk)-1] == '(':
    #             c = ')'
    #         else:
    #             c = '('

    #     if c == ')':
    #         if len(stk) == 0:
    #             is_OK = False
    #             break

    #         tmp = stk.pop()
    #         if tmp != '(':
    #             is_OK = False
    #             break
    #     else:
    #         stk.append(c)

    # if not is_OK:
    #     print('NO')
    # else:
    #     print('YES')
