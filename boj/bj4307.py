import sys

inputs = sys.stdin.readlines()

idx = 1

while idx < len(inputs):
    l, n = map(int, inputs[idx].split())
    idx += 1

    ants = list()
    for i in range(n):
        ants.append(int(inputs[idx]))
        idx += 1

    mins = list()
    maxs = list()
    for ant in ants:
        minn, maxx = ant, abs(l - ant)
        if minn > maxx:
            minn, maxx = maxx, minn

        mins.append(minn)
        maxs.append(maxx)

    print(max(mins), max(maxs))
