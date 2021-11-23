n = int(input())
board = list()
for i in range(n):
    board.append(input())

r, c = 0, 0
for i in range(n):
    chk = board[i].split('X')
    for cc in chk:
        if len(cc) >= 2:
            r += 1

    chk = ''.join([board[j][i] for j in range(n)]).split('X')
    for cc in chk:
        if len(cc) >= 2:
            c += 1
print(r, c)
