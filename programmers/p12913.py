def solution(land):
    dp = [[0, 0, 0, 0]]
    for i in range(len(land)):
        dp.append(list())
        for j in range(4):
            chk = {0, 1, 2, 3}
            chk.discard(j)
            max_last = -1
            for a in chk:
                max_last = max(max_last, dp[i][a])
            dp[i+1].append(land[i][j]+max_last)
    return max(dp[len(land)])
