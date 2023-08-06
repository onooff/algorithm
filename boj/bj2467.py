import sys

inputs = sys.stdin.readlines()
l = sorted(list(map(int, inputs[1].rstrip().split())))

best = float("inf")
best_couple = (0, 0)
a = 0
b = len(l) - 1
while a != b:
    d = abs(l[a] + l[b])
    if d < best:
        best = d
        best_couple = (l[a], l[b])
    if l[a] + l[b] > 0:
        b -= 1
    elif l[a] + l[b] < 0:
        a += 1
    else:
        break
print(best_couple[0], best_couple[1])
