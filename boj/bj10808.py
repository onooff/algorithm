s = input()
l = [0 for _ in range(26)]
for c in s:
    l[ord(c)-97] += 1
print(' '.join(map(str, l)))
