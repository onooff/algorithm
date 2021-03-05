t = int(input())

for tc in range(t):
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    ans = 0
    idx = 0
    dp = list()
    for num in l:
        dp.append(0)
        ans += num
        while num % x == 0:
            num //= x
            dp[idx] += 1

    is_end = False
    while not is_end:
        idx = 0
        for num in l:
            if dp[idx] == 0:
                is_end = True
                break
            ans += num
            dp[idx] -= 1
            idx += 1
    print(ans)
'''
44 66 88 22 22
8 12 16 4 4
20 20 4
44

4 6 8 2
2 3 4 1

'''
