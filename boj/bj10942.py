import sys

inputs = sys.stdin.readlines()
n, m = int(inputs[0]), int(inputs[2])
l = list(map(int, inputs[1].split()))
memo = {i: {i} for i in range(n)}
for i in range(n):
    left = i - 1
    right = i + 1
    while left >= 0 and right < n and l[left] == l[right]:
        memo[left].add(right)
        left -= 1
        right += 1
    if i + 1 < n and l[i] == l[i + 1]:
        memo[i].add(i + 1)
        left = i - 1
        right = i + 2
        while left >= 0 and right < n and l[left] == l[right]:
            memo[left].add(right)
            left -= 1
            right += 1
for i in range(3, len(inputs)):
    s, e = map(lambda x: int(x) - 1, inputs[i].split())
    if s in memo and e in memo[s]:
        print(1)
    else:
        print(0)
