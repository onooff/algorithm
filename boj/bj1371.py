import sys
inputs = sys.stdin.readlines()
d = dict()
for s in inputs:
    s = s.rstrip()
    for c in s:
        if c == ' ':
            continue
        d.setdefault(c, 0)
        d[c] += 1
maxx = max(d.values())
ans = list()
for k in d:
    if d[k] == maxx:
        ans.append(k)
ans.sort()
print(''.join(ans))
