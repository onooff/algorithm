board = [True, False, False]

s = input()

for c in s:
    if c == 'A':
        board[0], board[1] = board[1], board[0]
    elif c == 'B':
        board[1], board[2] = board[2], board[1]
    elif c == 'C':
        board[0], board[2] = board[2], board[0]

for i in range(3):
    if board[i]:
        print(i+1)
        break
