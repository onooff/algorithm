t = int(input())

for tc in range(t):
    n, w1, w2 = map(int, input().split())
    b1 = n-w1
    b2 = n-w2
    board = [[w1, w2], [b1, b2]]
    w, b = map(int, input().split())
    dominos = [w, b]
    ans = 'yes'
    for i in range(2):
        # while dominos[i] > 0:
        if board[i][0] > 0 and board[i][1] > 0:
            min_val = min(board[i][0], board[i][1])
            board[i][0] -= min_val
            board[i][1] -= min_val
            dominos[i] = max(0, dominos[i]-min_val)
        # else:
        if dominos[i] > 0:
            if (board[i][0] >= 2*dominos[i]) or (board[i][1] >= 2*dominos[i]):
                continue
            else:
                ans = 'no'
        if ans == 'no':
            break
    print(ans)
