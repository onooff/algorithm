str1 = input()
str2 = input()
dp = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i] == str2[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

i += 1
j += 1
print(dp[i][j])

"""
res = list()
while dp[i][j] > 0:
    if dp[i][j] == dp[i - 1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j - 1]:
        j -= 1
    else:
        res.append(str1[i - 1])
        i -= 1
        j -= 1
print("".join(reversed(res)))
"""
