import sys

input = sys.stdin.readline

r, c = map(int, input().split())
board = list()
fq = list()
jq = list()
for i in range(r):
    board.append(list(input().rstrip()))
    for j in range(c):
        if board[i][j] == "F":
            fq.append((i, j))
        elif board[i][j] == "J":
            jq.append((i, j))

d = ((0, 1), (0, -1), (1, 0), (-1, 0))

time = 0
esc = False
while (len(fq) or len(jq)) and not esc:
    time += 1

    nfq = list()
    while len(fq) > 0:
        y, x = fq.pop()
        for nd in d:
            ny = y + nd[0]
            nx = x + nd[1]
            if 0 <= ny < r and 0 <= nx < c and board[ny][nx] == ".":
                board[ny][nx] = "F"
                nfq.append((ny, nx))
    fq = nfq

    njq = list()
    while len(jq) > 0:
        y, x = jq.pop()
        for nd in d:
            ny = y + nd[0]
            nx = x + nd[1]
            if not (0 <= ny < r and 0 <= nx < c):
                esc = True
                break
            elif board[ny][nx] == ".":
                board[ny][nx] = "J"
                njq.append((ny, nx))
    jq = njq

if esc:
    print(time)
else:
    print("IMPOSSIBLE")
