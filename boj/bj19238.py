import sys

board = list()
n = 0
dx, dy = [0, -1, 1, 0], [-1, 0, 0, 1]


def isIn(ny, nx):
    global n
    if (ny < 0) | (ny >= n) | (nx < 0) | (nx >= n):
        return False
    else:
        return True


def bfsToDest(guest):  # 손님 시작점에서 도착점까지 거리 계산 bfs
    # print(guest)

    global board, n, dx, dy
    chk = [[False for col in range(n)] for row in range(n)]

    queue = [(guest[0], guest[1], 0)]
    chk[guest[0]][guest[1]] = True

    while queue:
        y, x, d = queue.pop(0)
        if (guest[2] == y) & (guest[3] == x):
            # print(guest, d)
            return d

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # print('>>', ny, nx)
            if isIn(ny, nx):
                # print(">> isin ok")
                if (board[ny][nx] != 1):
                    # print(">> not wall")
                    if (chk[ny][nx] == False):
                        # print('>>> in q')
                        chk[ny][nx] = True
                        queue.append((nx, ny, d+1))

    print("-1")
    sys.exit()


def bfsFindGuest(ti, tj):  # 택시 시작점에서 손님찾기
    global board, n, dx, dy
    chk = [[False for col in range(n)] for row in range(n)]

    queue = [(ti, tj, 0)]
    chk[ti][tj] = True

    while queue:
        y, x, d = queue.pop(0)
        # print('>>', y, x, d)

        if type(board[y][x]) != int:
            return [board[y][x][0], d]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if isIn(ny, nx):
                if (board[ny][nx] != 1):
                    if (chk[ny][nx] == False):
                        chk[ny][nx] = True
                        queue.append((ny, nx, d+1))
                        # print('>>>>in', ny, nx, d+1)

    print("-1")
    sys.exit()


'''
a, b = map(int, input().split())
print(a+b)

첫줄에 N,M 초기연료
다음부터 N*N Map
운전시작하는 좌표(행,열)
다음부터 M명 손님데이터
승객출발지(행,열) 승객도착지(행,열)
'''

n, m, oil = map(int, input().split())

for i in range(n):
    board.append(list(map(int, input().split())))
# print(board)

ti, tj = map(int, input().split())
ti -= 1
tj -= 1  # 좌표 1,1->0,0으로 맞춰줌

guests = []
for i in range(m):
    guest = input().split()
    guest[0] = int(guest[0])-1
    guest[1] = int(guest[1])-1
    guest[2] = int(guest[2])-1
    guest[3] = int(guest[3])-1  # 좌표 1,1->0,0으로 맞춰줌
    board[guest[0]][guest[1]] = [i, '태워주시오']

    guest.append(bfsToDest(guest))  # 손님 데이터에 도착지까지 거리 넣기 만약 안되는 경우 있으면 여기서 리턴
    guests.append(guest)


# print(n, m, oil)
# print(board)
# print(tj, ti)
# print(guests)

'''
bfs로 손님찾기
찾은 손님의 위치까지 가기 & 도착지까지 갈 수 있는지 계산
    가능-> 도착지로 택시좌표 이동, 손님삭제, 첫째줄로 가서 반복
    불가능-> -1
'''

ok = 0
while ok != m:
    # print(">>", oil)
    g = bfsFindGuest(ti, tj)  # return [board[y][x][0], d]
    if g[1]+guests[g[0]][4] > oil:
        # print("기름업따!", oil, g[1]+guests[g[0]][4])
        print("-1")
        sys.exit()
    # print(board[guests[g[0]][0]][guests[g[0]][1]], "얘태우고감", guests[g[0]])
    oil = oil-(g[1]+guests[g[0]][4])+guests[g[0]][4]*2
    board[guests[g[0]][0]][guests[g[0]][1]] = 0
    ti = guests[g[0]][2]
    tj = guests[g[0]][3]
    ok += 1

print(oil)
