import sys

maxx = -1
y, x = 0, 0
for i in range(9):
    l = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(9):
        if maxx < l[j]:
            maxx = l[j]
            y, x = i, j
print(f"{maxx}\n{y+1} {x+1}")
