def solution(numbers, target):
    d = dict()
    d.setdefault(0, 1)
    for n in numbers:
        nd = dict()
        for k in d:
            tmp = k+n
            if tmp not in nd:
                nd.setdefault(tmp, d[k])
            else:
                nd[tmp] += d[k]
            tmp = k-n
            if tmp not in nd:
                nd.setdefault(tmp, d[k])
            else:
                nd[tmp] += d[k]
        d = nd
    print(d)
    if target in d:
        return d[target]
    else:
        return 0


# print(solution(	[1, 1, 1, 1, 1], 3))
