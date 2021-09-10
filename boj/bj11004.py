import sys
inputs = sys.stdin.readlines()
n, k = map(int, inputs[0].rstrip().split())
l = list(map(int, inputs[1].rstrip().split()))
l.sort()
print(l[k-1])
