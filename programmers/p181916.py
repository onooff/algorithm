from collections import defaultdict


def solution(a, b, c, d):
    dic = defaultdict(int)
    for n in [a, b, c, d]:
        dic[n] += 1
    k = sorted(list(dic.keys()))
    if len(k) == 1:
        return k[0] * 1111
    elif len(k) == 2:
        if dic[k[0]] == 2:
            return (k[0] + k[1]) * (k[1] - k[0])
        else:
            kk = 0
            if dic[k[1]] == 3:
                kk = 1
            return (10 * k[kk] + k[(0 if kk == 1 else 1)]) ** 2
    elif len(k) == 3:
        ret = 1
        for n in k:
            if dic[n] == 1:
                ret *= n
        return ret
    else:
        return min(k)
