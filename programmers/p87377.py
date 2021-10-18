def solution(line):
    inf = 999999999
    size = len(line)
    p = set()
    x_list = list()
    y_list = list()
    for i in range(size-1):
        for j in range(i+1, size):
            a, b, c = line[i]
            d, e, f = line[j]
            pp = a*e
            qq = b*d
            if pp == qq:
                continue
            d1 = pp-qq
            d2 = qq-pp
            dd1 = b*f-e*c
            dd2 = a*f-c*d
            if dd1 % d1 == 0 and dd2 % d2 == 0:
                x = dd1//d1
                y = dd2//d2
                x_list.append(x)
                y_list.append(y)
    minx, miny, maxx, maxy = min(x_list), min(y_list), max(x_list), max(y_list)
    dx = maxx-minx+1
    dy = maxy-miny+1
    print(dx, dy)
    board = [[False for _ in range(dx)] for _ in range(dy)]
    for i in range(len(x_list)):
        # print(v)
        board[len(board)-(y_list[i]-miny)-1][x_list[i]-minx] = True
    for i in range(len(board)):
        tmp = ''
        for j in range(len(board[i])):
            if board[i][j]:
                tmp += '*'
            else:
                tmp += '.'
        board[i] = tmp
        # print(board[i])
    # board.reverse()
    return board
