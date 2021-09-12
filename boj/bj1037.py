import sys
l = list(map(int, sys.stdin.readlines()[1].rstrip().split()))
l.sort()
print(l[0]*l[len(l)-1])
