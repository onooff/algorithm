import sys

l = list()
max_len = 0
for i in range(5):
    l.append(input())
    max_len = max(max_len, len(l[i]))

for i in range(max_len):
    for s in l:
        if i < len(s):
            sys.stdout.write(s[i])
