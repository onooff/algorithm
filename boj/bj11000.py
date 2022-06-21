import sys
inputs = sys.stdin.readlines()
q = list()
for i in range(1, len(inputs)):
    s, e = map(int, inputs[i].split())
    q.append((s, 1))
    q.append((e, 0))
q.sort()
cur_cnt = 0
max_cnt = 0
for cur in q:
    if cur[1] == 1:
        cur_cnt += 1
    else:
        cur_cnt -= 1
    max_cnt = max(max_cnt, cur_cnt)
print(max_cnt)
