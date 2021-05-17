def solution(s):
    answer = []
    for ss in s:
        stk = ''
        cnt = 0
        for i in range(len(ss)):
            if ss[i] == '0':
                if stk[-2:] == '11':
                    stk = stk[:-2]
                    cnt += 1
                else:
                    stk += '0'
            else:
                stk += '1'
        # print(cnt)
        # print('>>>', stk)
        here = 0
        for i in range(len(stk)+1):
            if i == len(stk):
                i -= here
                break
            if stk[i] == '0':
                here = 0
            else:
                here += 1
                if here == 3:
                    i -= 2
                    break
        print(i)
        stk1 = stk[:i]
        stk2 = stk[i:]
        s_110 = ''
        for i in range(cnt):
            s_110 += '110'
        # answer.append((stk1, s_110, stk2))
        answer.append(stk1+s_110+stk2)

    return answer


print(solution(	["1110", "100111100", "0111111010"]))
