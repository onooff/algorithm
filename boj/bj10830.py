MAX_B = 100000000000
n, b = map(int, input().split())
matrix = list()
# um = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
for i in range(n):
    matrix.append(list(map(lambda x: int(x) % 1000, input().split())))


def mul_maxrix(a, b, d=1):
    if len(a[0]) != len(b):
        return None
    l = len(a[0])
    y = len(a)
    x = len(b[0])
    ret = [[0 for _ in range(x)] for _ in range(y)]
    for i in range(y):
        for j in range(x):
            for k in range(l):
                ret[i][j] += a[i][k] * b[k][j]
            ret[i][j] %= d
    return ret


memo = {1: [[matrix[i][j] for j in range(n)] for i in range(n)]}
d = 2
while d < MAX_B:
    memo[d] = mul_maxrix(memo[d // 2], memo[d // 2], 1000)
    d *= 2
k = sorted(memo.keys(), key=lambda x: -x)

b -= 1
while b > 0:
    i = 0
    while k[i] > b:
        i += 1
    matrix = mul_maxrix(matrix, memo[k[i]], 1000)
    b -= k[i]

for i in range(n):
    for j in range(n):
        if j == n - 1:
            print(matrix[i][j])
        else:
            print(matrix[i][j], end=" ")
