import sys

inputs = sys.stdin.readlines()

s = inputs[0].rstrip()
love = list("LOVE")
default_d = {c: 0 for c in love}
for c in s:
    if c in default_d:
        default_d[c] += 1
names = sorted(list(map(lambda x: x.rstrip(), inputs[2:])))
maxx = -1
ans = None
for name in names:
    d = {c: default_d[c] for c in default_d}
    for c in name:
        if c in d:
            d[c] += 1
    tmp = 1
    for i in range(3):
        for j in range(i + 1, 4):
            tmp *= d[love[i]] + d[love[j]]
            if tmp == 0:
                break
    tmp %= 100
    if tmp > maxx:
        maxx = tmp
        ans = name
print(ans)
