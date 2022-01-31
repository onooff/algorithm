import sys
inputs = sys.stdin.readlines()
board = [list() for _ in range(4)]
chk = set()
ans = list()
for i in range(1, len(inputs)):
    cur = list(map(int, inputs[i].rstrip().split()))
    for i in range(4):
        board[i].append((cur[i+1], cur[0]))
for b in board:
    b.sort(key=lambda x: (-x[0], x[1]))
    for p in b:
        if p[1] not in chk:
            chk.add(p[1])
            ans.append(str(p[1]))
            break
print(' '.join(ans))
