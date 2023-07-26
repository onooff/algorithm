s = list(input())
s.reverse()
n = 0
while len(s) > 0:
    n += 1
    ns = list(str(n))
    for c in ns:
        if c == s[-1]:
            s.pop()
            if len(s) == 0:
                break
print(n)
