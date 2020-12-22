n, m = map(int, input().split())

logs = list(map(int, input().split()))

low = 0
high = max(logs)
mid = 0
get_log = 0
ans = -1
while low <= high:
    mid = (high+low)//2
    get_log = 0
    for log in logs:
        if log-mid > 0:
            get_log += log-mid
    # print(">>>", mid, get_log)
    if get_log < m:
        high = mid-1
    elif get_log > m:
        low = mid+1
        ans = max(ans, mid)
    elif get_log == m:
        ans = max(ans, mid)
        break

print(ans)
