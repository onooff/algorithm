INF = float("inf")
LENGTH = 100001
board = [INF for i in range(LENGTH)]
n, k = map(int, input().split())


def is_in(n, LENGTH):
    return 0 <= n < LENGTH


board[n] = 0
min_val = INF
min_cnt = 0
q = [(n, 0)]
while len(q) > 0 and min_val >= q[0][1]:
    cur, val = q.pop(0)
    # print(cur, val)
    if val > board[cur]:
        continue
    if cur == k:
        if min_val > val:
            min_val = val
            min_cnt = 0
        if min_val == val:
            min_cnt += 1
    nxt_val = board[cur] + 1
    for nxt in [cur + 1, cur - 1, cur * 2]:
        if is_in(nxt, LENGTH) and board[nxt] >= nxt_val:
            board[nxt] = nxt_val
            q.append((nxt, nxt_val))

print(min_val)
print(min_cnt)
