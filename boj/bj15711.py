# 골드바흐의 추측 = 2초과 짝수는 두 소수의 합으로 나타낼 수 있음
import sys

lim = 2000001
primes = {i for i in range(3, lim, 2)}
for i in range(3, lim):
    if i in primes:
        for j in range(i + i, lim, i):
            primes.discard(j)
primes.add(2)
primes_list = list(primes)
primes_list.sort()

inputs = sys.stdin.readlines()

for i in range(1, len(inputs)):
    a, b = map(int, inputs[i].rstrip().split())
    ab = a + b
    chk = ab % 2
    ans = False
    if ab <= 3:
        pass
    elif chk == 0:
        ans = True
    else:
        ab -= 2
        if ab <= primes_list[-1]:
            if ab in primes:
                ans = True
        else:
            ans = True
            for prime in primes_list:
                if ab % prime == 0:
                    ans = False
                    break
    if ans:
        sys.stdout.write("YES\n")
    else:
        sys.stdout.write("NO\n")
