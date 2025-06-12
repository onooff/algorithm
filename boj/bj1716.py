import sys

input = sys.stdin.readline

while True:
    n, k = map(int, input().split())
    if n == k == -1:
        break

    l = list(map(int, input().split()))
    for i in range(n, k - 1, -1):
        l[i - k] -= l[i]
        l[i] = 0

    while len(l) > 0 and l[-1] == 0:
        l.pop()
    if len(l) == 0:
        print(0)
    else:
        print(" ".join(map(str, l)))
