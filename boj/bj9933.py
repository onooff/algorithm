import sys
inputs = sys.stdin.readlines()
inputs.pop(0)
for i in range(len(inputs)):
    inputs[i] = inputs[i].rstrip()
inputs = set(inputs)
for s in inputs:
    if ''.join(reversed(s)) in inputs:
        print(len(s), s[len(s)//2])
        break
