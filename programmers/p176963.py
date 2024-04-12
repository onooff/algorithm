def solution(name, yearning, photo):
    d = dict()
    for i in range(len(name)):
        d[name[i]] = yearning[i]
    ans = []
    for p in photo:
        summ = 0
        for n in p:
            if n in d:
                summ += d[n]
        ans.append(summ)
    return ans
