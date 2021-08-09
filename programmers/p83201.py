def grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 50:
        return 'D'
    else:  # elif 50 > score:
        return 'F'


def solution(scores):
    d = len(scores)
    ans = str()
    for i in range(d):
        sum_s = 0
        min_s = 999999
        min_cnt = 1
        max_s = -1
        max_cnt = 1
        for j in range(d):
            now = scores[j][i]
            sum_s += now
            if min_s == now:
                min_cnt += 1
            elif min_s > now:
                min_s = now
                min_cnt = 1
            if max_s == now:
                max_cnt += 1
            elif max_s < now:
                max_s = now
                max_cnt = 1
        if (min_s == scores[i][i] and min_cnt == 1) or (max_s == scores[i][i] and max_cnt == 1):
            ans += grade((sum_s-scores[i][i])/(d-1))
        else:
            ans += grade(sum_s/d)
    return ans


print(solution([[90, 50], [50, 90]]))
