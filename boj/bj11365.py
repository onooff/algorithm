import sys
inputs = sys.stdin.readlines()
inputs.pop()
for line in inputs:
    sys.stdout.write(line.rstrip()[::-1]+'\n')
