def solution(s):
    answer = ''
    ls = list(s)
    idx = 0
    while idx < len(ls):
        c = ls[idx]
        if c.isdigit():
            answer += c
            idx += 1
        elif c == 'z':
            answer += '0'
            idx += 4
        elif c == 'o':
            answer += '1'
            idx += 3
        elif c == 't':
            if ls[idx+1] == 'w':
                answer += '2'
                idx += 3
            elif ls[idx+1] == 'h':
                answer += '3'
                idx += 5
        elif c == 'f':
            if ls[idx+1] == 'o':
                answer += '4'
                idx += 4
            elif ls[idx+1] == 'i':
                answer += '5'
                idx += 4
        elif c == 's':
            if ls[idx+1] == 'i':
                answer += '6'
                idx += 3
            elif ls[idx+1] == 'e':
                answer += '7'
                idx += 5
        elif c == 'e':
            answer += '8'
            idx += 5
        elif c == 'n':
            answer += '9'
            idx += 4
        # print(answer)
    return int(answer)


# print(solution("2three45sixseven"))
# zero,one,two,three,four,five,six,seven,eight,nine
