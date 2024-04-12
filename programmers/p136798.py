import math


def solution(number, limit, power):
    ans = 0

    for num in range(1, number + 1):
        cnt = 0
        for d in range(1, int(math.sqrt(num)) + 1):
            if num % d == 0:
                if num // d != d:
                    cnt += 2
                else:
                    cnt += 1

        if cnt > limit:
            ans += power
        else:
            ans += cnt

    return ans
