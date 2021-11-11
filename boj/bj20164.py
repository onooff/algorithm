import math

s = input()
q = [[s, 0]]
idx = 0

maxx = -math.inf
minn = math.inf
while idx < len(q):
    cur = q[idx]
    idx += 1
    odd = cur[1]
    for c in cur[0]:
        odd += int(c) % 2
    if len(cur[0]) > 2:
        for i in range(1, len(cur[0])-1):
            for j in range(i+1, len(cur[0])):
                q.append(
                    [str(int(cur[0][:i])+int(cur[0][i:j])+int(cur[0][j:])), odd])
    elif len(cur[0]) == 2:
        q.append([str(int(cur[0][0])+int(cur[0][1])), odd])
    else:
        maxx = max(maxx, odd)
        minn = min(minn, odd)

print(minn, maxx)
