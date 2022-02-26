import sys
inputs = sys.stdin.readlines()
memo = dict()
for i in range(1, len(inputs)):
    n = int(inputs[i])
    if n not in memo:
        memo[n] = n*n
    print(memo[n])
