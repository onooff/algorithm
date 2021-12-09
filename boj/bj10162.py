n = int(input())
if n % 10 != 0:
    print(-1)
else:
    a, b, c = 0, 0, 0
    a = n//300
    n %= 300
    b = n//60
    n %= 60
    c = n//10
    print(a, b, c)
