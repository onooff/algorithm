import math


def solution(begin, end):
    answer = []
    if begin == 1:
        answer.append(0)
        begin += 1
    for i in range(begin, end+1):
        answer.append(1)
        for j in range(2, int(math.sqrt(i))):
            if i % j == 0:
                tmp = i//j
                if tmp <= 10000000:
                    answer[-1] = tmp
                    break
    return answer
