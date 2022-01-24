a, b = map(int, input().split())
p, q = b-a, b

d = 2
while d <= p and d <= q:
    if p % d == q % d == 0:
        p //= d
        q //= d
    else:
        d += 1

print(p, q)
