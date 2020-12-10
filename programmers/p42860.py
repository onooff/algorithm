def solution(name):
    answer = 0

    name = list(name)
    check = []
    for i in range(len(name)):
        check.append('A')

    i = 0
    while name != check:
        l = 0
        r = 0
        while name[boundary(len(name), i-l)] == 'A':
            l += 1
        while name[boundary(len(name), i+r)] == 'A':
            r += 1
        if l >= r:
            i = boundary(len(name), i+r)
            answer += r
            answer += change(name[i])
            name[i] = 'A'
        else:
            i = boundary(len(name), i-l)
            answer += l
            answer += change(name[i])
            name[i] = 'A'
    return answer


def change(c):
    # print(c, ord(c)-ord('A'), ord('Z')-ord(c)+1)
    return min(ord(c)-ord('A'), ord('Z')-ord(c)+1)


def boundary(l, n):
    n = n % l
    if n >= 0:
        return n
    else:
        return l+n


# print(solution("BBBB"))
