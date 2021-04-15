def solution(a, b):
    answer = 0

    a.sort()
    b.sort()
    go = len(a)
    for i in range(go):
        ab = a[0]*b[len(b)-1]
        ba = b[0]*a[len(a)-1]
        if ab > ba:
            answer += ba
            b.pop(0)
            a.pop()
        else:
            answer += ab
            a.pop(0)
            b.pop()

    return answer
