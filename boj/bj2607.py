import sys

inputs = sys.stdin.readlines()

d = dict()
for c in inputs[1].rstrip():
    d.setdefault(c, 0)
    d[c] += 1

cnt = 0
for i in range(2, len(inputs)):
    dd = dict()
    for c in inputs[i].rstrip():
        dd.setdefault(c, 0)
        dd[c] += 1

    diff_under = 0
    diff_over = 0
    visit = set()
    for k in dd.keys():
        if k in d:
            visit.add(k)
            diff = d[k] - dd[k]
            if diff > 0:
                diff_under += diff
            elif diff < 0:
                diff_over -= diff

        else:
            diff_over += dd[k]
        if diff_under >= 2 or diff_over >= 2:
            break
    for k in d.keys():
        if k not in visit:
            diff_under += d[k]
    if diff_under < 2 and diff_over < 2:
        cnt += 1
        # print(inputs[i].rstrip(), dd, diff_under, diff_over)

print(cnt)
