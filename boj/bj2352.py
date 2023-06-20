input()
li = list(map(int, input().split()))
dp = [li[0]]
dp_nums = {li[0]}
for i in range(1, len(li)):
    if li[i] in dp_nums:
        continue

    if li[i] > dp[-1]:
        dp.append(li[i])
        dp_nums.add(li[i])
    else:
        l = 0
        r = len(dp)
        mid = (l+r)//2
        while l < r:
            # print(i, '=', li[i], l, mid, r)
            if dp[mid] < li[i]:
                l = mid+1
            else:
                r = mid
            mid = (l+r)//2
        dp_nums.discard(dp[mid])
        dp_nums.add(li[i])
        dp[mid] = li[i]
    # print(dp, dp_nums)
print(len(dp))


'''
#시간빠른코드
import sys
input = sys.stdin.readline
from bisect import bisect_left as bs #<-신기하다

input()
lis = [0]
for d in map(int, input().split()):
    if lis[-1] < d:
        lis.append(d)
    else:
        lis[bs(lis, d)] = d
print(len(lis)-1)
'''
