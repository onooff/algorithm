import sys

inputs = sys.stdin.readlines()

n = int(inputs[0])
m = int(inputs[1])
l = list(map(int, inputs[2].split()))

ans = max(l[0], n - l[-1])
for i in range(len(l) - 1):
    d = l[i + 1] - l[i]
    ans = max(ans, d // 2 + d % 2)
print(ans)
