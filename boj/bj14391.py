n, m = map(int, input().split())
board = [list(map(int, list(input()))) for _ in range(n)]
maxx = -1
for chk in range(2 ** (n * m)):
    b = format(chk, "b")
    b = ("0" * (n * m - len(b))) + b
    b = [b[k * m : k * m + m] for k in range(n)]

    summ = 0
    for i in range(n):
        tmp = 0
        for j in range(m):
            if b[i][j] == "0":
                summ += tmp
                tmp = 0
            else:
                tmp = tmp * 10 + board[i][j]
        summ += tmp

    for j in range(m):
        tmp = 0
        for i in range(n):
            if b[i][j] == "1":
                summ += tmp
                tmp = 0
            else:
                tmp = tmp * 10 + board[i][j]
        summ += tmp
    maxx = max(maxx, summ)

print(maxx)
