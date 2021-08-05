n, m = map(int, input().split())
print(min((n-1)+(m-1)*n, (m-1)+(n-1)*m))
