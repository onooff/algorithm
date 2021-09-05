import math
n = int(input())
l = list(map(int, input().split()))
b, c = map(int, input().split())
answer = 0
for a in l:
    # if b > c:
    answer += 1
    a = max(0, a-b)
    answer += math.ceil(a/c)
    # else:
    #     answer += math.ceil(a/c)
print(answer)
