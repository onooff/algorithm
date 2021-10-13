import sys
inputs = sys.stdin.readlines()
n, m = int(inputs[0]), int(inputs[2])
l = list(map(int, inputs[1].split()))
pd = dict()
for i in range(n):
    s = i
    e = i
    while s >= 0 and e < n:
        if l[s] == l[e]:
            pd.setdefault(s, set())
            pd[s].add(e)
            s -= 1
            e += 1
        else:
            break
    if i+1 < n and l[i] == l[i+1]:
        s = i
        e = i+1
        while s >= 0 and e < n:
            if l[s] == l[e]:
                pd.setdefault(s, set())
                pd[s].add(e)
                s -= 1
                e += 1
            else:
                break

for i in range(3, m+3):
    s, e = map(int, inputs[i].split())
    s, e = s-1, e-1
    if s in pd and e in pd[s]:
        print(1)
    else:
        print(0)
