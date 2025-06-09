N,M = map(int, input().split())
l = [0 for _ in range(N)]
for _ in range(M):
    i,j,k = map(int, input().split())
    for num in range(i-1,j):
        l[num] = k;
print(' '.join(list(map(str, l))))
