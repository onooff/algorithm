import sys

input = sys.stdin.readline

n, m = map(int, input().split())
s = set()
for _ in range(n):
    s.add(input().rstrip())
for _ in range(m):
    l = list(input().rstrip().split(","))
    for word in l:
        if word in s:
            s.discard(word)
    print(len(s))
