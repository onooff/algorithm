import copy


def solution(info, query):
    언어 = dict()
    직군 = dict()
    경력 = dict()
    음식 = dict()
    점수 = list()
    idx = -1

    for i in info:
        idx += 1
        i = i.split()
        if i[0] not in 언어:
            언어.setdefault(i[0], set())
        언어[i[0]].add(idx)
        if i[1] not in 직군:
            직군.setdefault(i[1], set())
        직군[i[1]].add(idx)
        if i[2] not in 경력:
            경력.setdefault(i[2], set())
        경력[i[2]].add(idx)
        if i[3] not in 음식:
            음식.setdefault(i[3], set())
        음식[i[3]].add(idx)
        점수.append(int(i[4]))

    answer = []
    d = {i for i in range(len(info))}
    for q in query:
        ans = copy.deepcopy(d)
        q = q.split()
        if q[0] != '-':
            ans = ans & 언어[q[0]]
        if q[2] != '-':
            ans = ans & 직군[q[2]]
        if q[4] != '-':
            ans = ans & 경력[q[4]]
        if q[6] != '-':
            ans = ans & 음식[q[6]]
        count = 0
        qn = int(q[7])
        for n in ans:
            if 점수[n] >= qn:
                count += 1
        answer.append(count)
    return answer


print(
    solution(
        ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
            "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
        ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250",
            "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]
    )
)
