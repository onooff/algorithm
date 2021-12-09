import sys
inputs = sys.stdin.readlines()
cy = 100
sd = 100
for i in range(1, len(inputs)):
    c, s = map(int, inputs[i].rstrip().split())
    if c > s:
        sd -= c
    elif c < s:
        cy -= s
print(cy)
print(sd)
