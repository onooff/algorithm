v = {'a', 'e', 'i', 'o', 'u'}
s = input()
cnt = 0
for c in s:
    if c in v:
        cnt += 1
print(cnt)
