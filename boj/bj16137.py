'''
5 5
1 1 1 1 1
0 6 0 0 0
1 1 0 1 1
1 1 0 1 1
1 1 0 1 1
'''

n, m = map(int, input().split())
board = list()
for i in range(n):
    board.append(list(map(int, input().split())))

ans = 0
s = set()
s.add((0, 0, False))
end = False
while not end:
    ns = set()
    while len(s) > 0:
        tmp = s.pop()
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]:
            ny = tmp[0]+d[0]
            nx = tmp[1]+d[1]
            if ny == n-1 and nx == n-1:
                end = True
                break
            if ny >= 0 and nx >= 0 and ny < n and nx < n:
                if board[ny][nx] == 1:
                    ns.add((ny, nx, tmp[2]))
                elif board[tmp[0]][tmp[1]] == 1:
                    if board[ny][nx] != 0:
                        if (ans+1) % board[ny][nx] == 0:
                            ns.add((ny, nx, tmp[2]))
                    else:
                        if (ans+1) % m == 0 and not tmp[2]:
                            ns.add((ny, nx, True))
        if end:
            break
    ans += 1
    s = ns
    # if ans == 18:
    #     print(s)
print(ans)
