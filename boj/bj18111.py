n, m, b = map(int, input().split())
board_max = -1
board_min = 1000
board = list()
for i in range(n):
    board.append(list(map(int, input().split())))
    for h in board[i]:
        board_max = max(board_max, h)
        board_min = min(board_min, h)
# print(sum(list(map(sum, board))))


def calc(board, height, b):
    use_b = 0
    get_b = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] > height:
                get_b += board[i][j]-height
            else:
                use_b += height-board[i][j]
    if b+get_b < use_b:
        return False
    return(use_b+(get_b*2), height)


ans = calc(board, board_min, b)
for i in range(board_min+1, board_max+1):
    tmp = calc(board, i, b)
    if tmp != False:
        if ans[0] >= tmp[0]:
            ans = tmp
    else:
        break
print(ans[0], ans[1])
