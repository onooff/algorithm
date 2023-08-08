import sys

inputs = sys.stdin.readlines()

n, m = map(int, inputs[0].split())

d = dict()
for i in range(1, n + 1):
    name, power = inputs[i].split()
    power = int(power)
    if power not in d:
        d[power] = name
k = sorted(list(d.keys()))

answer = list()
for i in range(n + 1, len(inputs)):
    p = int(inputs[i])
    l = 0
    r = len(k) - 1
    ans = 0
    while l <= r:
        m = (l + r) // 2
        if p <= k[m]:
            r = m - 1
            ans = m
        else:
            l = m + 1
    answer.append(d[k[ans]])
print("\n".join(answer))
