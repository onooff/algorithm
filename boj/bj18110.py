import sys

not_bankers_round = lambda x: round(x + 0.0000001)

l = sorted(list(map(int, sys.stdin.readlines()[1:])))
lim = not_bankers_round(len(l) * 0.15)
if lim > 0:
    l = l[lim:-lim]
if len(l) > 0:
    print(not_bankers_round(sum(l) / len(l)))
else:
    print(0)
