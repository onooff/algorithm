def solution(n, left, right):
    answer = list()
    y = left//n
    x = (left % n)-1
    for i in range(left, right+1):
        x += 1
        if x == n:
            x = 0
            y += 1
        answer.append(max(x+1, y+1))
    return answer
