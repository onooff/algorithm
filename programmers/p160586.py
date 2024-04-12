def solution(keymap, targets):
    d = dict()
    for km in keymap:
        for i, c in enumerate(km):
            d.setdefault(c, float("inf"))
            d[c] = min(d[c], i + 1)

    ans = []
    for t in targets:
        summ = 0
        for c in t:
            if c not in d:
                summ = -1
                break
            summ += d[c]
        ans.append(summ)

    return ans
