import sys

inputs = sys.stdin.readlines()
l = list(map(int, inputs[1].rstrip().split()))

d = dict()
ans = 0
for i in range(len(l) - 1):
    for j in range(i + 1, len(l)):
        d.setdefault(l[i] + l[j], list())
        d[l[i] + l[j]].append((i, j))

for i in range(len(l)):
    if l[i] in d:
        for pair in d[l[i]]:
            if i not in pair:
                ans += 1
                break

print(ans)
