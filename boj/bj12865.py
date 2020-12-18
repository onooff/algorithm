n, k = map(int, input().split())
thing = list()
# is_pick = [False]*n
thing.append((0, 0))
for i in range(n):
    thing.append(tuple(map(int, input().split())))
# dp = [[0]*(k+1)]*(n+1)
dp = [[0 for j in range(k+1)] for i in range(n+1)]
for i in range(1, n+1):  # 물건번호
    for j in range(1, k+1):  # 짐꾼힘
        if j-thing[i][0] >= 0:
            dp[i][j] = max(dp[i-1][j], thing[i][1]+dp[i-1][j-thing[i][0]])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k])
# print(thing)
# for i in range(n+1):
#     print(dp[i])


# max_v = 0

# thing.sort(key=lambda x: x[0])

# def dfs(now_k, now_v):
#     global n, k, thing, is_pick, max_v, cnt
#     for i in range(n):
#         if not is_pick[i]:
#             if now_k+thing[i][0] <= k:
#                 is_pick[i] = True
#                 dfs(now_k+thing[i][0], now_v+thing[i][1])
#                 is_pick[i] = False
#             else:
#                 cnt += 1
#                 max_v = max(now_v, max_v)
#                 print(cnt, max_v)
#                 return

# dfs(0, 0)
# print(max_v)

# dfs 할 경우 경우의수최대값 = 2^100 = 시간 초과
