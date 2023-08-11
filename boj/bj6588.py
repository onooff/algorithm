import sys

input = sys.stdin.readline

limit = 1000000
l = [True] * (limit + 1)
m = int(limit**0.5)
primes = list()
for i in range(2, m):
    if l[i]:
        for k in range(i + i, len(l), i):
            l[k] = False
for i in range(2, len(l)):
    if l[i]:
        primes.append(i)

ans = list()
while True:
    n = int(input())
    if n == 0:
        break
    for p in primes:
        if l[n - p]:
            ans.append(f"{n} = {p} + {n-p}")
            break
        elif n <= p:
            ans.append("Goldbach's conjecture is wrong.")
            break

print("\n".join(ans))
