'''
4
hello
hell
heaven
goodbye
3
hi
he
h
7
structure
structures
ride
riders
stress
solstice
ridiculous

2.00
1.67
2.71
'''
import sys

inputs = sys.stdin.readlines()
size = len(inputs)
idx = 0
while idx < size:
    n = int(inputs[idx])
    idx += 1
    start = idx
    d = dict()
    for _ in range(n):
        word = inputs[idx]
        idx += 1
        cur = d
        for c in word:
            cur.setdefault(c, dict())
            cur = cur[c]
    cnt = n
    for i in range(start, start+n):
        word = inputs[i]
        cur = d
        for i in range(len(word)-2):
            c = word[i]
            if len(cur[c]) != 1:
                cnt += 1
            cur = cur[c]
    print("{:.2f}".format(cnt/n))
