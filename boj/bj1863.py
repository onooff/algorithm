import sys

inputs = sys.stdin.readlines()

cnt = 0
stk = list()
for i in range(1, len(inputs)):
    w, h = map(int, inputs[i].rstrip().split())
    while len(stk) > 0 and stk[-1] > h:
        cnt += 1
        stk.pop()
    if h > 0 and (len(stk) == 0 or stk[-1] != h):
        stk.append(h)
print(cnt + len(stk))
