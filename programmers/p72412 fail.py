import pandas as pd


def solution(info, query):
    data = dict()
    data.setdefault('언어', list())
    data.setdefault('직군', list())
    data.setdefault('경력', list())
    data.setdefault('음식', list())
    data.setdefault('점수', list())
    for i in info:
        i = i.split()
        data['언어'].append(i[0])
        data['직군'].append(i[1])
        data['경력'].append(i[2])
        data['음식'].append(i[3])
        data['점수'].append(int(i[4]))
    df = pd.DataFrame(data)
    # print(df)

    answer = []
    for q in query:
        str_expr = ''
        q = q.split()
        if q[0] != '-':
            str_expr += f'(언어 == "{q[0]}") and '
        if q[2] != '-':
            str_expr += f'(직군 == "{q[2]}") and '
        if q[4] != '-':
            str_expr += f'(경력 == "{q[4]}") and '
        if q[6] != '-':
            str_expr += f'(음식 == "{q[6]}") and '
        str_expr += f'(점수 >= {q[7]})'
        answer.append(len(df.query(str_expr)))

    return answer


print(
    solution(
        ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
            "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
        ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250",
            "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]
    )
)
