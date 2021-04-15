def solution(s):
    answer = ''
    words = list(s.split(' '))
    print(words)
    for word in words:
        if word == '':
            answer += ' '
            continue
        if str.isalpha(word[0]):
            answer += str.upper(word[0])+str.lower(word[1:])+' '
        else:
            answer += word+' '
    return answer[:-1]


print(solution('test  test'))
