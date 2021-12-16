# 사용한 로프 중 가장 약한 로프*로프개수가 들수있는 최대 중량
import sys

inputs = sys.stdin.readlines()
n = int(inputs[0])
ropes = list(map(int, inputs[1:]))
ropes.sort()
maxx = -1
for i in range(n):
    maxx = max(maxx, ropes[i] * (n - i))
print(maxx)
