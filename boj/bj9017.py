import sys

inputs = sys.stdin.readlines()[1:]
for i in range(1, len(inputs), 2):
    l = list(map(int, inputs[i].split()))
    d = dict()
    for team in l:
        d.setdefault(team, 0)
        d[team] += 1
    ok = set()
    for team in d.keys():
        if d[team] >= 6:
            ok.add(team)

    d = dict()
    p = 1
    for team in l:
        if team in ok:
            d.setdefault(team, list())
            d[team].append(p)
            p += 1
    print(sorted(list(d.keys()), key=lambda x: (sum(d[x][:4]), d[x][4]))[0])
