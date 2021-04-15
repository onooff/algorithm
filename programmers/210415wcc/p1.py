def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        j = 1
        if not signs[i]:
            j = -1
        answer += absolutes[i]*j
    return answer
