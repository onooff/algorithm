# t = int(input())
# d = [[0, 1], [0, -1], [1, 0], [-1, 0]]

# for tc in range(t):
#     n = int(input())
#     l = list()
#     chk = list()
#     for i in range(2):
#         l.append(list(map(int, input().split())))
#         chk.append(list())
#         for j in l[i]:
#             chk[i].append(0)
#     ans = -1

#     def dfs(si, sj, sum):
#         global n, l, chk, ans
#         if 0 not in set(chk[0]) and 0 not in set(chk[1]):
#             ans = max(ans, sum)
#             return

#         for i in range(si, 2):
#             for j in range(sj, n):
#                 if chk[i][j] == 0:
#                     chk[i][j] += 1
#                     for dd in d:
#                         ni = i+dd[0]
#                         nj = j+dd[1]
#                         if (ni >= 0 and nj >= 0 and ni < 2 and nj < n):
#                             chk[ni][nj] += 1
#                     dfs(0, 0, sum+l[i][j])
#                     for dd in d:
#                         ni = i+dd[0]
#                         nj = j+dd[1]
#                         if (ni >= 0 and nj >= 0 and ni < 2 and nj < n):
#                             chk[ni][nj] -= 1
#                     chk[i][j] -= 1

#     dfs(0, 0, 0)
#     print(ans)


t = int(input())
d = [[0, 1], [0, -1], [1, 0], [-1, 0]]

for tc in range(t):
    n = int(input())
    l = list()
    for i in range(2):
        l.append(list(map(int, input().split())))

    dp = [list(), list()]

    dp[0].append(0)
    dp[0].append(l[0][0])
    dp[1].append(0)
    dp[1].append(l[1][0])

    for x in range(2, n+1):
        dp[0].append(max(dp[1][x-1], dp[1][x-2])+l[0][x-1])
        dp[1].append(max(dp[0][x-1], dp[0][x-2])+l[1][x-1])
    # print('>>>', dp[0])
    # print('>>>', dp[1])
    print(max(dp[0][n], dp[1][n]))
