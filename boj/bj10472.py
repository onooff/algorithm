import sys

input = sys.stdin.readline
t = int(input())

flip_pos = [
    [0, 1, 3],
    [0, 1, 2, 4],
    [1, 2, 5],
    [0, 3, 4, 6],
    [1, 3, 4, 5, 7],
    [2, 4, 5, 8],
    [3, 6, 7],
    [4, 6, 7, 8],
    [5, 7, 8],
]
flip = {"*": ".", ".": "*"}
end = "........."

for _ in range(t):
    start = input().rstrip() + input().rstrip() + input().rstrip()
    if start == end:
        print(0)
        continue
    q = [start]
    visit = {start}
    idx = 0
    nq = list()
    step = 0
    is_end = False
    while idx < len(q):
        cur = q[idx]
        idx += 1

        cur_board = list(cur)
        for fp in flip_pos:
            for pos in fp:
                cur_board[pos] = flip[cur_board[pos]]
            chk = "".join(cur_board)
            if chk == end:
                print(step + 1)
                is_end = True
            if chk not in visit:
                visit.add(chk)
                nq.append(chk)
            for pos in fp:
                cur_board[pos] = flip[cur_board[pos]]
        if is_end:
            break
        if idx == len(q) and len(nq) > 0:
            q = nq
            nq = list()
            idx = 0
            step += 1
