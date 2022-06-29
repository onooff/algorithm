primes = {i for i in range(2, 1000001)}
for i in range(2, 1000001):
    if i in primes:
        d = i+i
        while d < 1000001:
            primes.discard(d)
            d += i

squares = sorted(list(map(lambda x: x*x, primes)))

minn, maxx = map(int, input().split())

r = {i for i in range(minn, maxx+1)}
for sq in squares:
    d = minn//sq
    if minn % sq != 0:
        d += 1
    num = sq*d
    while num <= maxx:
        r.discard(num)
        num += sq
print(len(r))
# print(r)
