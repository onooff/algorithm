f, s, g, u, d = map(int, input().split())
chk = {s}
q = [s]
nq = []
idx = 0
cnt = 0
is_ans = False
while len(q) > 0:
    cur = q[idx]
    if cur == g:
        is_ans = True
        break
    idx += 1
    up, down = cur+u, cur-d
    if up <= f and up not in chk:
        chk.add(up)
        nq.append(up)
    if down > 0 and down not in chk:
        chk.add(down)
        nq.append(down)
    if idx == len(q):
        idx = 0
        q = nq
        nq = []
        cnt += 1

if is_ans:
    print(cnt)
else:
    print('use the stairs')
