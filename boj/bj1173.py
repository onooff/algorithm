'''
N-운동해야하는시간
m-초기맥박
M-최대맥박
T-운동시증가맥박
R-휴식시증가맥박
'''

import math
N, m, M, T, R = map(int, input().split())

if m+T > M:
    print(-1)
else:
    cnt = 0
    now = m
    while N > 0:
        cnt += 1
        if now+T <= M:
            N -= 1
            now += T
        else:
            now = max(m, now-R)
    print(cnt)
