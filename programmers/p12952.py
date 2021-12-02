def dfs(board, qps, cur):
    if cur >= len(board):
        return 1
    ret = 0
    nxt = list(qps)
    for n in nxt:
        is_ok = True
        for i in range(cur):
            l = n-(cur-i)
            r = n+(cur-i)
            if (l > -1 and board[i] == l) or (r < len(board) and board[i] == r):
                is_ok = False
                break
        if is_ok:
            board[cur] = n
            qps.discard(n)
            ret += dfs(board, qps, cur+1)
            qps.add(n)
    return ret


def solution(n):
    # return [0,1,0,0,2,10,4,40,92,352,724,2680,14200][n]

    board = [None for _ in range(n)]
    queen_pos_set = {i for i in range(n)}

    return dfs(board, queen_pos_set, 0)
