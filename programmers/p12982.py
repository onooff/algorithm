def solution(d, budget):
    answer = 0
    d.sort()
    for dd in d:
        if budget-dd < 0:
            break
        budget -= dd
        answer += 1
    return answer
