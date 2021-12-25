import sys

inputs = sys.stdin.readlines()

n, m = map(int, inputs[0].rstrip().split())
board = [inputs[i].rstrip() for i in range(1, len(inputs))]
d = {"U": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1)}

esc = set()
not_esc = set()

for i in range(n):
    for j in range(m):
        y = i
        x = j
        v = (i, j)
        if v in esc or v in not_esc:
            continue
        trail = set()
        is_esc = False
        while v not in trail:
            trail.add(v)
            ny = y + d[board[y][x]][0]
            nx = x + d[board[y][x]][1]
            if 0 <= ny < n and 0 <= nx < m:
                y = ny
                x = nx
                v = (ny, nx)
                if v in esc:
                    is_esc = True
                    break
                elif v in not_esc:
                    break
            else:
                is_esc = True
                break
        # print(i, j, trail)
        if is_esc:
            esc |= trail
        else:
            not_esc |= trail
# print(esc, not_esc)
print(len(esc))
