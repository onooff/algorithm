import sys
inputs = sys.stdin.readlines()
h, w = map(int, inputs[0].rstrip().split())
board = inputs[1:]
h_set = {x for x in range(h)}
w_set = {x for x in range(w)}
for i in range(h):
    for j in range(w):
        if board[i][j] == 'X':
            h_set.discard(i)
            w_set.discard(j)
print(max(len(h_set), len(w_set)))
