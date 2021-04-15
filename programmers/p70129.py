def solution(s):
    answer = [0, 0]
    while s != '1':
        zero_romoved_s = ''
        cnt = 0
        for i in range(len(s)):
            if s[i] == '0':
                cnt += 1
            else:
                zero_romoved_s += s[i]
        answer[0] += 1
        answer[1] += cnt
        # print(bin(len(zero_romoved_s)))
        s = str(bin(len(zero_romoved_s)))[2:]
    return answer


# print(solution('110010101001'))
