def rotate_board(board=[[]]):
    rotated_board = [[0 for _ in range(len(board))]
                     for _ in range(len(board[0]))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            rotated_board[j][len(board)-i-1] = board[i][j]
    return rotated_board


def solution(game_board, table):
    pieces = dict()
    d = ((1, 0), (-1, 0), (0, 1), (0, -1))
    n, m = len(table), len(table[0])
    for i in range(n):
        for j in range(m):
            if table[i][j] == 1:
                piece = [(0, 0)]
                table[i][j] = 0

                idx = 0
                while idx < len(piece):
                    y = piece[idx][0]
                    x = piece[idx][1]
                    idx += 1
                    for nd in d:
                        ny = y+nd[0]
                        nx = x+nd[1]
                        if 0 <= ny+i < n and 0 <= nx+j < m and table[ny+i][nx+j] == 1:
                            piece.append((ny, nx))
                            table[ny+i][nx+j] = 0
                piece = tuple(piece)
                pieces.setdefault(piece, 0)
                pieces[piece] += 1

    answer = 0
    for k in range(4):
        n, m = len(game_board), len(game_board[0])
        chk = set()
        for i in range(n):
            for j in range(m):
                if game_board[i][j] == 0 and (i, j) not in chk:
                    space = [(0, 0)]
                    chk.add((i, j))
                    idx = 0
                    while idx < len(space):
                        y = space[idx][0]
                        x = space[idx][1]
                        idx += 1
                        for nd in d:
                            ny = y+nd[0]
                            nx = x+nd[1]
                            v = (ny, nx)
                            chk_v = (ny+i, nx+j)
                            if 0 <= ny+i < n and 0 <= nx+j < m and game_board[ny+i][nx+j] == 0 and chk_v not in chk:
                                space.append(v)
                                chk.add(chk_v)
                    space = tuple(space)
                    if space in pieces:
                        # print(space, i, j)
                        answer += len(space)
                        pieces[space] -= 1
                        if pieces[space] == 0:
                            pieces.pop(space)
                        for s in space:
                            game_board[i+s[0]][j+s[1]] = 1
        if k < 3:
            game_board = rotate_board(game_board)
        # print("rotated")
        # for i in range(len(game_board)):
        #     print(game_board[i])
    return answer


# print(solution(
#     [
#         [1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
#         [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
#         [1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
#         [1, 0, 0, 1, 0, 0, 1, 1, 1, 1],
#         [1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
#         [1, 1, 0, 0, 0, 1, 1, 1, 0, 1],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#     ],
#     [
#         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#         [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
#         [0, 0, 1, 0, 0, 1, 1, 1, 0, 0],
#         [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
#         [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     ]
# ))
