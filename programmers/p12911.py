def solution(n):
    b = list(str(bin(n))[2:])
    is_ans = False
    cnt_0 = 0
    if b[-1] == '0':
        cnt_0 = 1
    for i in range(len(b)-2, -1, -1):
        if b[i] == '0' and b[i+1] == '1':
            b[i] = '1'
            b[i+1] = '0'

            for j in range(i+2, len(b)):
                # print('>>>', cnt_0)
                if cnt_0 > 0:
                    b[j] = '0'
                    cnt_0 -= 1
                else:
                    b[j] = '1'
            is_ans = True
            break
        if b[i] == '0':
            cnt_0 += 1
    if not is_ans:
        b.insert(1, '0')
        for i in range(len(b)-1, 1, -1):
            if b[i] == '0' and b[i-1] == '1':
                b[i] = '1'
                b[i-1] = '0'
                break
    # print(''.join(b))
    return int(''.join(b), 2)


print(solution(6))
