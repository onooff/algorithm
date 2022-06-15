answer = []


def hanoi(n, cur, target):
    global answer
    if n == 1:
        answer.append([cur, target])
        return target
    for i in range(1, 4):
        if i != cur and i != target:
            prev = hanoi(n-1, cur, i)
            break
    answer.append([cur, target])
    hanoi(n-1, prev, target)
    return target


def solution(n):
    global answer
    hanoi(n, 1, 3)
    return answer
