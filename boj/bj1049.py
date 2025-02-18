n, m = map(int, input().split())
l = list()
min_six = float("inf")
min_one = float("inf")
for _ in range(m):
    six, one = map(int, input().split())
    min_six = min(six, min_six)
    min_one = min(one, min_one)
if min_one * 6 < min_six:
    min_six = min_one * 6
ans = 0
ans += (n // 6) * min_six
if (n % 6) > 0:
    if (n % 6) * min_one < min_six:
        ans += (n % 6) * min_one
    else:
        ans += min_six
print(ans)
