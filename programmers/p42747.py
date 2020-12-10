def solution(citations):
    citations.sort()
    # print(citations)
    for h in range(len(citations), 0, -1):
        for i in range(len(citations)):
            if citations[i] >= h:
                if len(citations)-i >= h and i <= h:
                    return h
    return 0


print(solution([0]))
'''
5번 이상 인용된 논문이 2편
5번 이상 인용된 논문이 2편
3번 이상 인용된 논문이 3편 ok
'''
