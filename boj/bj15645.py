n = int(input())

board = list()
for i in range(n):
    board.append(list(map(int, input().split())))
mindp = [[board[0][0], board[0][1], board[0][2]]]
maxdp = [[board[0][0], board[0][1], board[0][2]]]
for i in range(1, n):
    mindp.append([
        min(mindp[i-1][0], mindp[i-1][1])+board[i][0],
        min(mindp[i-1][0], mindp[i-1][1], mindp[i-1][2])+board[i][1],
        min(mindp[i-1][1], mindp[i-1][2])+board[i][2],
    ])
    maxdp.append([
        max(maxdp[i-1][0], maxdp[i-1][1])+board[i][0],
        max(maxdp[i-1][0], maxdp[i-1][1], maxdp[i-1][2])+board[i][1],
        max(maxdp[i-1][1], maxdp[i-1][2])+board[i][2],
    ])
    # print(mindp[i-1])
    # print(maxdp[i-1])
print(max(maxdp[n-1][0], maxdp[n-1][1], maxdp[n-1][2]),
      min(mindp[n-1][0], mindp[n-1][1], mindp[n-1][2]))
