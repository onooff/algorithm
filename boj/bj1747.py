import math
import bisect

R = 1003002
primes = {i for i in range(2, R)}

for i in range(math.ceil(math.sqrt(R))):
    if i in primes:
        d = i * 2
        while d < R:
            primes.discard(d)
            d += i

for n in list(primes):
    is_palindrome = True
    s = str(n)
    for j in range(len(s) // 2):
        if s[j] != s[-(j + 1)]:
            is_palindrome = False
            break
    if not is_palindrome:
        primes.discard(n)

primes = sorted(primes)

N = int(input())
print(primes[bisect.bisect_left(primes, N)])
