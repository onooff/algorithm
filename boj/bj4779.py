import sys


def go(l, start, end):
    d = end-start
    if d == 1:
        return
    d3 = d//3
    for i in range(start+d3, end-d3):
        l[i] = ' '
    go(l, start, start+d3)
    go(l, end-d3, end)


inputs = sys.stdin.readlines()
for i in range(len(inputs)):
    n = int(inputs[i])
    l = ['-' for i in range(3**n)]
    go(l, 0, 3**n)
    print(''.join(l))
