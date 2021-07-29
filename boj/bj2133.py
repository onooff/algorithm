n = int(input())

if n % 2 == 1:
    print(0)
else:
    n //= 2
    dp = [1]
    for i in range(1, n+1):
        dp.append(dp[i-1]*3)
        for j in range(i-1):
            dp[i] += dp[j]*2
    print(dp)
    print(dp[n])
