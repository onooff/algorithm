N, M = map(int, input().split())
l = [_ for _ in range(1, N + 1)]
for _ in range(M):
    i, j = map(int, input().split())
    for num in range((j - i + 1) // 2):
        l[i - 1 + num], l[j - 1 - num] = l[j - 1 - num], l[i - 1 + num]
print(" ".join(list(map(str, l))))
