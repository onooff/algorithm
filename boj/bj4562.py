import sys
inputs = sys.stdin.readlines()
answer = {True: "MMM BRAINS", False: "NO BRAINS"}
for i in range(1, len(inputs)):
    x, y = map(int, inputs[i].split())
    print(answer[x >= y])
