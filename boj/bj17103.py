primes = {i for i in range(3, 1000000, 2)}
primes.add(2)
for num in range(3, 1000000//2+1):
    d = num+num
    while d < 1000000:
        primes.discard(d)
        d += num
primes_list = sorted(list(primes))

t = int(input())
for _ in range(t):
    cnt = 0
    num = int(input())
    lim = num//2
    for p in primes_list:
        if p > lim:
            break
        if num-p in primes:
            cnt += 1
    print(cnt)
