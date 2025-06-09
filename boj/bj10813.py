N, M = map(int, input().split())
l = [_ for _ in range(1, N + 1)]
for _ in range(M):
    i, j = map(int, input().split())
    l[i - 1], l[j - 1] = l[j - 1], l[i - 1]
print(" ".join(list(map(str, l))))
