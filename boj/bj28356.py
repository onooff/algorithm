# n, m = map(int, input().split())
# board = [[0 for _ in range(m)] for _ in range(n)]

# d = (
#     (-1, -1),
#     (-1, 0),
#     (-1, 1),
#     (0, -1),
#     (0, 1),
#     (1, -1),
#     (1, 0),
#     (1, 1),
# )

# maxx = 0
# for i in range(n):
#     for j in range(m):
#         chk = set()
#         for nd in d:
#             ny = i + nd[0]
#             nx = j + nd[1]
#             if 0 <= ny < n and 0 <= nx < m:
#                 chk.add(board[ny][nx])
#         for k in range(1, 11):
#             if k not in chk:
#                 board[i][j] = k
#                 if maxx < k:
#                     maxx = k
#                 break

# print(maxx)
# for b in board:
#     print(*b)

n, m = map(int, input().split())
if n == 1 and m == 1:
    print("1\n1")
elif n == 1 or m == 1:
    print(2)
    num = [1, 2]
    cur = 0
    for i in range(n):
        for j in range(m):
            print(num[cur], end=" ")
            cur = (cur + 1) % 2
        print()
else:
    print(4)
    num = [[1, 2], [3, 4]]
    x, y = 0, 0
    for i in range(n):
        s = list()
        for j in range(m):
            s.append(str(num[x][y]))
            y = (y + 1) % 2
        print(" ".join(s))
        x = (x + 1) % 2
        y = 0
