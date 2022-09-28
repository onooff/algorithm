def solution(survey, choices):
    answer = ['R', 'C', 'J', 'A']
    pair = ['RT', 'CF', 'JM', 'AN']
    d = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    for i in range(len(survey)):
        point = choices[i] - 4
        c = survey[i][0]
        if point > 0:
            c = survey[i][1]
        d[c] += abs(point)
    for i in range(len(pair)):
        p = pair[i]
        if d[p[1]] > d[p[0]]:
            answer[i] = p[1]
    return ''.join(answer)
