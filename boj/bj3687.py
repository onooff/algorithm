import sys


inf = 999999999999999
num = [inf, inf, 1, 7, 4, 2, 0, 8]
dp = [inf for i in range(101)]
dp[2] = 1
dp[3] = 7
dp[4] = 4
dp[5] = 2
dp[6] = 6
dp[7] = 8
for i in range(8, len(dp)):
    for j in range(2, 8):
        dp[i] = min(
            dp[i],
            int(str(num[j] if j != 6 else 6) + str(dp[i - j])),
            int(str(dp[i - j]) + str(num[j])),
        )

inputs = sys.stdin.readlines()
answer = list()
for i in range(1, len(inputs)):
    n = int(inputs[i])
    maxx = ["1" for _ in range(n // 2)]
    if n % 2 == 1:
        maxx[0] = "7"

    answer.append(f"{dp[n]} {''.join(maxx)}")
print(*answer, sep="\n")
