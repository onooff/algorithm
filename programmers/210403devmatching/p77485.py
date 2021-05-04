def solution(rows, columns, queries):
    answer = []
    n = 1
    board = list()
    for i in range(rows):
        board.append(list())
        for j in range(columns):
            board[i].append(n)
            n += 1
    # print(board)
    for q in queries:
        ub = q[0]-1
        lb = q[1]-1
        db = q[2]-1
        rb = q[3]-1
        tmp = board[ub][lb]
        tmptmp = 0
        min_val = 9999999
        for j in range(lb, rb):
            min_val = min(min_val, tmp)
            tmptmp = board[ub][j+1]
            board[ub][j+1] = tmp
            tmp = tmptmp
        for i in range(ub, db):
            min_val = min(min_val, tmp)
            tmptmp = board[i+1][rb]
            board[i+1][rb] = tmp
            tmp = tmptmp
        for j in range(rb, lb, -1):
            min_val = min(min_val, tmp)
            tmptmp = board[db][j-1]
            board[db][j-1] = tmp
            tmp = tmptmp
        for i in range(db, ub, -1):
            min_val = min(min_val, tmp)
            tmptmp = board[i-1][lb]
            board[i-1][lb] = tmp
            tmp = tmptmp
        min_val = min(min_val, tmp)
        for i in board:
            print(i)
        print()
        answer.append(min_val)

    return answer


print(solution(	6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
