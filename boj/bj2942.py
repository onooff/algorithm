n, m = map(int, input().split())
a, b = max(n, m), min(n, m)

while True:
    r = a % b
    a, b = b, r
    if b == 0:
        break

d = 1
answer = list()
while d * d <= a:
    if a % d == 0:
        answer.append(f"{d} {n//d} {m//d}")
        dd = a // d
        if dd != d:
            answer.append(f"{dd} {n//dd} {m//dd}")
    d += 1

print(*answer, sep="\n")
