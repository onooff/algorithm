t = int(input())

for tc in range(t):
    n = int(input())
    board = list(map(int, input().split()))
    dp = [0 for i in range(n+1)]
    board.insert(0, 0)
    ans = -1
    for i in range(len(board)-1, 0, -1):
        now = i
        point = 0
        while now < len(board):
            if dp[now] != 0:
                point += dp[now]
                break
            point += board[now]
            now += board[now]
        dp[i] = point
        ans = max(ans, point)
    print(ans)
