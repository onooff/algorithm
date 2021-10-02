import sys
inputs = sys.stdin.readlines()
x, y, m = map(int, inputs[0].rstrip().split())
e = list()
h = list()
for i in range(x):
    e.append((i+1, int(inputs[i+1])))
for i in range(y):
    h.append((i+1, int(inputs[i+1+x])))
e.sort(key=lambda x: -x[1])
h.sort(key=lambda x: -x[1])

cur = m
ans = list()
e_idx = 0
h_idx = 0
while (len(e) > e_idx or len(h) > h_idx) and cur > 0:
    if len(h) > h_idx and (len(e) <= e_idx or cur+h[h_idx][1] <= m):
        cur += h[h_idx][1]
        ans.append(h[h_idx][0])
        h_idx += 1
    else:
        cur -= e[e_idx][1]
        ans.append(-e[e_idx][0])
        e_idx += 1

if cur > 0:
    for a in ans:
        print(a)
else:
    print(0)
