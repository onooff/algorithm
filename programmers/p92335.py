import math


def solution(n, k):
    ans = 0
    s = ''
    while n > 0:
        s = str((n % k))+s
        n = n // k
    s = s.split('0')
    memo = {2: 1}
    for num in s:
        if num == '' or num == '1':
            continue
        num = int(num)
        if num in memo:
            ans += memo[num]
            continue
        if num % 2 == 0:
            continue
        memo[num] = 1
        for d in range(3, int(math.sqrt(num))+1, 2):
            if num % d == 0:
                memo[num] = 0
                break
        ans += memo[num]
    return ans
