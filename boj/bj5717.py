import sys
inputs = sys.stdin.readlines()
for i in range(len(inputs)-1):
    print(sum(map(int, inputs[i].rstrip().split())))
