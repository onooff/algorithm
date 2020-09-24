def solution(n, lost, reserve):
    answer = 0
    for l in lost:
        if l in reserve:
            reserve.remove(l)
            lost.remove(l)

    answer = n - len(lost)

    # for l in lost:
    #     if l+1 in reserve:
    #         reserve.remove(l+1)
    #         answer += 1
    #     elif l-1 in reserve:
    #         reserve.remove(l-1)
    #         answer += 1

    flag = True
    while flag:
        flag = False
        for r in reserve:
            if (r-1 in lost) & (r+1 in lost):
                pass
            elif r-1 in lost:
                lost.remove(r-1)
                reserve.remove(r)
                answer += 1
                flag = True
            elif r+1 in lost:
                lost.remove(r+1)
                reserve.remove(r)
                answer += 1
                flag = True

    return answer


print(solution(	5, [2, 4], [1, 3, 5]))
