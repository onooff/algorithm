import sys

input = sys.stdin.readline


def main():
    n = int(input())
    x = []
    s = 0
    for _ in range(n):
        a, b = map(int, input().split())
        x.append((a, b))
        s += a * b
    if s % 2:
        return 0
    t = s // 2
    old = [0] * (s + 1)
    old[0] = 1
    m = 0
    x.sort(key=lambda i: -i[1])
    for key, value in x:
        tmp = key * (value + 1)
        for i in range(min(m, t), -1, -1):
            if old[i] and not old[i + key]:
                old[i + key : i + tmp : key] = [1] * value
        if old[t]:
            return 1
        m += tmp - key
    return 0


for i in range(3):
    print(main())
import sys

inputs = sys.stdin.readlines()

answer = list()
idx = 0
for _ in range(3):
    n = int(inputs[idx])
    idx += 1
    l = list()
    summ = 0
    for _ in range(n):
        money, mount = map(int, inputs[idx].rstrip().split())
        idx += 1
        summ += money * mount
        l.append((money, mount))

    if summ % 2 == 1:
        answer.append(0)
        continue

    ans = summ // 2
    dp = [0 for _ in range(ans + 1)]
    dp[0] = 1

    for info in l:
        money, mount = info
        for n in range(ans, money - 1, -1):
            if dp[n - money]:
                for j in range(mount):
                    if n + money * j <= ans:
                        dp[n + money * j] = 1
                    else:
                        break

    answer.append(dp[-1])
print(*answer, sep="\n")
