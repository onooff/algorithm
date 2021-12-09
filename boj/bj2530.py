h, m, s = map(int, input().split())
t = int(input())

a = s+m*60+h*3600+t
s = a % 60
a //= 60
m = a % 60
a //= 60
h = a % 24
print(h, m, s)
