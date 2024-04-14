def solution(board, h, w):
    answer = 0
    for d in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        ny = h + d[0]
        nx = w + d[1]
        if (
            0 <= ny < len(board)
            and 0 <= nx < len(board[0])
            and board[ny][nx] == board[h][w]
        ):
            answer += 1
    return answer
