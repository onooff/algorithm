d = ((1, 0), (-1, 0), (0, 1), (0, -1))


def is_in(y, x, n, m):
    return 0 <= y < n and 0 <= x < m


def print_board(board, q):
    for i in range(len(board)):
        for j in range(len(board[i])):
            n = board[i][j]
            if n == 2:
                print("□", end="")
            elif n == 1:
                if (i, j) in q:
                    print("●", end="")
                else:
                    print("■", end="")
            elif n == 0:
                print(" ", end="")
        print()
    print()


n, m = map(int, input().split())
board = list()
for i in range(n):
    board.append(list(map(int, input().split())))


# 치즈를 녹일 수 있는 외부공기를 표현하는 값을 0->2로 치환
# 가장자리에는 치즈가 놓이지 않는다는 문제조건이 있었으므로 (0,0)은 외부공기임이 보장됨. 여기부터 BFS
# 함수로 작성하여 풀이 과정 중 내부공기를 외부공기로 바꿔야 할 때 재사용
def air(board, d, i, j, nq=None, visited=None):
    q = [(i, j)]
    while len(q) > 0:
        y, x = q.pop()
        board[y][x] = 2
        for nd in d:
            ny = y + nd[0]
            nx = x + nd[1]
            np = (ny, nx)
            if is_in(ny, nx, n, m):
                if board[ny][nx] == 0:
                    q.append(np)
                elif board[ny][nx] == 1 and nq != None:
                    air_cnt = 0
                    for nnd in d:
                        if board[ny + nnd[0]][nx + nnd[1]] == 2:
                            air_cnt += 1
                    if air_cnt >= 2 and np not in visited:
                        visited.add(np)
                        nq.append(np)


air(board, d, 0, 0)

# 보드를 전체 순회하여 다음 틱에 녹을 치즈를 큐에 넣어 bfs 준비
visited = set()
q = list()
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            air_cnt = 0
            for nd in d:
                # 가장자리는 치즈가 없다고 문제에서 보장되었으므로 치즈인 좌표에서는 is_in 체크할 필요 없음
                if board[i + nd[0]][j + nd[1]] == 2:
                    air_cnt += 1
            if air_cnt >= 2:
                np = (i, j)
                visited.add(np)
                q.append(np)

nq = list()
ans = 0
while len(q) > 0:
    y, x = q.pop(0)
    board[y][x] = 2
    for nd in d:
        ny = y + nd[0]
        nx = x + nd[1]
        if board[ny][nx] == 0:
            air(board, d, ny, nx, nq, visited)
    for nd in d:
        ny = y + nd[0]
        nx = x + nd[1]
        np = (ny, nx)
        if board[ny][nx] == 1:
            air_cnt = 0
            for nnd in d:
                if board[ny + nnd[0]][nx + nnd[1]] == 2:
                    air_cnt += 1
            if air_cnt >= 2 and np not in visited:
                visited.add(np)
                nq.append(np)
    if len(q) == 0:
        ans += 1
        q = nq
        nq = list()
        # print(q)
        # print_board(board, q)

print(ans)
