'''
7 8
a#c#eF.1
.#.#.#..
.#B#D###
0....F.1
C#E#A###
.#.#.#..
d#f#bF.1
'''

import sys
inputs = sys.stdin.readlines()
n, m = map(int, inputs[0].rstrip().split())
board = list()
chk = list()
start = tuple()
for i in range(n):
    board.append(list(inputs[i+1].rstrip()))
    chk.append([set() for j in range(m)])
    j = inputs[i+1].find('0')
    if j >= 0:
        start = (i, j, (0, 0, 0, 0, 0, 0))
        board[i][j] = '.'
mapping = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5}
d = ((0, 1), (0, -1), (1, 0), (-1, 0))
q = [start]
chk[start[0]][start[1]].add(start[2])
is_ans = False
walk = 0
now = 1
nxt = 0
while len(q) > 0:
    cur = q.pop(0)
    now -= 1
    y = cur[0]
    x = cur[1]
    keys = cur[2]
    for dd in d:
        ny = y+dd[0]
        nx = x+dd[1]
        if (0 <= ny < n and 0 <= nx < m):
            c = board[ny][nx]
            is_ok = True
            new_key = False
            if c == '#':
                is_ok = False
            elif c.isalpha():
                if c.isupper():
                    c = c.lower()
                    if keys[mapping[c]] == 0:
                        is_ok = False
                else:
                    new_key = True
            elif c == '1':
                is_ans = True
                walk += 1
                break
            if is_ok:
                if new_key and keys[mapping[c]] == 0:
                    nk = list(keys)
                    nk[mapping[c]] = 1
                    nk = tuple(nk)
                    if nk not in chk[ny][nx]:
                        q.append((ny, nx, nk))
                        chk[ny][nx].add(nk)
                        nxt += 1
                elif keys not in chk[ny][nx]:
                    q.append((ny, nx, keys))
                    chk[ny][nx].add(keys)
                    nxt += 1
    if is_ans:
        break
    if now == 0:
        now = nxt
        nxt = 0
        walk += 1
if is_ans:
    print(walk)
else:
    print(-1)
