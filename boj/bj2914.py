# 38 24 875

a, b = map(int, input().split())
print(min(a*b, (a*(b-1))+1))
