import math

n = int(input())
l = list(map(int, input().split()))
t, p = map(int, input().split())

print(sum(list(map(lambda x: math.ceil(x / t), l))))
print(f"{n // p} {n % p}")
