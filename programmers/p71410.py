def solution(new_id):
    # 1
    new_id = str.lower(new_id)
    answer = list(new_id)
    # 2,3
    idx = 0
    while idx < len(answer):
        if idx > 0 and answer[idx] == '.' and answer[idx-1] == '.':
            answer.pop(idx)
        else:
            chk = answer[idx]
            if not str.islower(chk) and not str.isdigit(chk) and chk != '-' and chk != '_' and chk != '.':
                answer.pop(idx)
            else:
                idx += 1
    # 4
    if len(answer) > 0:
        if answer[0] == '.':
            answer.pop(0)
    if len(answer) > 0:
        if answer[len(answer)-1] == '.':
            answer.pop()
    # 5
    if len(answer) == 0:
        answer.append('a')
    # 6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[len(answer)-1] == '.':
            answer.pop()
    # 7
    # print('>>>', answer)
    while len(answer) < 3:
        answer.append(answer[len(answer)-1])
    ret = ''
    for c in answer:
        ret += c
    return ret


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
