def solution(info, query):
    answer = []
    info_split = []
    for i in info:
        info_split.append(i.split(" "))
    # print(info_split)
    '''
    0:언어
    1:백프론트
    2:경력
    3:음식
    4:점수
    '''

    for q in query:
        result = 0
        check_Index = []
        qs = ((q.replace("and", "")).replace("  ", " ")).split(" ")
        print(qs)
        for i in range(0, 4):
            if qs[i] != "-":
                check_Index.append(i)
        print(check_Index)
        for e in info_split:
            isOk = True
            for i in check_Index:
                if e[i] != qs[i]:
                    isOk = False
                    break
            if not isOk:
                continue
            if int(e[4]) >= int(qs[4]):
                print(e[4], qs[4])
                result += 1
        answer.append(result)

    return answer


print(solution(	["java backend junior pizza 150",
                 "python frontend senior chicken 210",
                 "python frontend senior chicken 150",
                 "cpp backend senior pizza 260",
                 "java backend junior chicken 80",
                 "python backend senior chicken 50"],
                ["java and backend and junior and pizza 100",
                 "python and frontend and senior and chicken 200",
                 "cpp and - and senior and pizza 250",
                 "- and backend and senior and - 150",
                 "- and - and - and chicken 100",
                 "- and - and - and - 150"]))
