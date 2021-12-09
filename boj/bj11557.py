import sys
inputs = sys.stdin.readlines()
t = int(inputs[0])
idx = 1
for _ in range(t):
    best = ''
    maxx = -1
    n = int(inputs[idx])
    idx += 1
    for _ in range(n):
        name, drink = inputs[idx].rstrip().split()
        idx += 1
        drink = int(drink)
        if drink > maxx:
            best = name
            maxx = drink
    print(best)
