import sys
import math

inputs = sys.stdin.readlines()
n = int(inputs[0])
trees = list(map(int, inputs[1:]))
trees.sort()

gaps = set()
for i in range(1, n):
    gaps.add(trees[i] - trees[i - 1])
gaps = list(gaps)
gaps.sort()

gcd = gaps[0]
for i in range(1, len(gaps)):
    gcd = math.gcd(gcd, gaps[i])

print((trees[-1] - trees[0]) // gcd - n + 1)
