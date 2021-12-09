import sys
n = int(input())
while n != -1:
    s = set()
    for i in range(1, n):
        if n % i == 0:
            s.add(i)
    if sum(s) == n:
        s = list(s)
        s.sort()
        sys.stdout.write(f"{n} = {s[0]}")
        for j in range(1, len(s)):
            sys.stdout.write(f" + {s[j]}")
        sys.stdout.write("\n")
    else:
        sys.stdout.write(f"{n} is NOT perfect.\n")
    n = int(input())
