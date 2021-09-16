coins = [500, 100, 50, 10, 5, 1]
change = 1000-int(input())
cnt = 0
for c in coins:
    while change >= c:
        change -= c
        cnt += 1
    if change == 0:
        break
print(cnt)
