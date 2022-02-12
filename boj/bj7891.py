import sys
inputs = sys.stdin.readlines()
for i in range(1, len(inputs)):
    print(sum(map(int, inputs[i].split())))
