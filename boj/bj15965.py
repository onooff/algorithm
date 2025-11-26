# import math

# cnt = 1
# n = 3
# while cnt < 500000:
#     is_prime = True
#     for d in range(2, math.ceil(n**0.5) + 1):
#         if n % d == 0:
#             is_prime = False
#             break
#     if is_prime:
#         cnt += 1
#         print(n, cnt)
#     n += 1
# print(n)

maxx = 7368788
primes = [_ for _ in range(2, maxx)]
set_primes = set(primes)
cnt = 1
for n in primes:
    if n in set_primes:
        # print(n, cnt)
        cnt += 1
        nn = n + n
        while nn <= maxx:
            set_primes.discard(nn)
            nn += n
primes = list(set_primes)
primes.sort()
# print(primes)

print(primes[int(input()) - 1])
