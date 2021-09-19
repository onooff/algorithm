n, m = map(int, input().split())
arr = list()
for _ in range(n):
    arr.append(list(map(int, input().split())))
k = int(input())
for _ in range(k):
    a, b, c, d = map(int, input().split())
    a, b = a-1, b-1
    ssum = 0
    for i in range(a, c):
        for j in range(b, d):
            ssum += arr[i][j]
    print(ssum)
