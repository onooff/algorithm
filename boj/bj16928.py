inf = 999999999
board = [inf for i in range(101)]
n, m = map(int, input().split())
warp = dict()
for i in range(n+m):
    s, e = map(int, input().split())
    warp.setdefault(s, e)

q = [1]
board[1] = 0

while len(q) > 0:
    now = q.pop(0)
    t = board[now]+1
    for go in range(now+1, now+7):
        if go > 100:
            break
        if go in warp:
            if board[go] > t:
                board[go] = t
            w = warp[go]
            if board[w] > t:
                board[w] = t
                q.append(w)
        else:
            if board[go] > t:
                board[go] = t
                q.append(go)
print(board[100])
# print(board)
