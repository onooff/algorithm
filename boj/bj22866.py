import sys

inputs = sys.stdin.readlines()

l = list(map(int, inputs[1].rstrip().split()))

stk = list()
cnt = [0 for _ in range(len(l))]
close_idx = [float("inf") for _ in range(len(l))]
for i in range(len(l)):
    while len(stk) > 0 and stk[-1][0] <= l[i]:
        stk.pop()
    if len(stk) > 0:
        cnt[i] += len(stk)
        if abs(close_idx[i] - i) > abs(stk[-1][1] - i):
            close_idx[i] = stk[-1][1]
    stk.append((l[i], i))

stk = list()
for i in range(len(l) - 1, -1, -1):
    while len(stk) > 0 and stk[-1][0] <= l[i]:
        stk.pop()
    if len(stk) > 0:
        cnt[i] += len(stk)
        if abs(close_idx[i] - i) > abs(stk[-1][1] - i):
            close_idx[i] = stk[-1][1]
    stk.append((l[i], i))

for i in range(len(l)):
    print(cnt[i], close_idx[i] + 1 if cnt[i] != 0 else "")
