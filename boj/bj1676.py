n = int(input())

cnt = 0
for i in range(1, n+1):
    while i % 5 == 0:
        cnt += 1
        i //= 5
print(cnt)
