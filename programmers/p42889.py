def solution(N, stages):
    '''
    확인 필요한 값
    해당 스테이지에 도전한 사람수
    해당스테이지 클리어하지 못한 사람 수
    '''

    stages.sort()
    checkStage = 1
    index = 0
    count = 0
    # clear = [0]*(N+1)
    # stuck = [0]*(N+1)
    failRate = list()
    for i in range(1, N+1):
        failRate.append((i, 0))

    while index < len(stages):
        if stages[index] > checkStage:
            # clear[checkStage] = len(stages)-index+count
            # stuck[checkStage] = count
            failRate[checkStage-1] = (
                checkStage, count/(len(stages)-index+count))
            checkStage += 1
            count = 0
            continue
        count += 1
        index += 1
    if count != 0 and checkStage <= N:
        failRate[checkStage-1] = (checkStage, count/(len(stages)-index+count))

    failRate = sorted(failRate, key=lambda x: -x[1])
    # print(stages)
    # print(failRate)

    # print(stuck)
    # print(clear)

    col1, _ = zip(*failRate)
    answer = list(col1)

    return answer


print(solution(4, [4, 4, 4, 4, 4]))
print(solution(4, [1, 1, 1, 1, 1]))
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
