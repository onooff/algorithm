import sys
inputs = sys.stdin.readlines()
for i in range(1, len(inputs)):
    n, s = inputs[i].split()
    sys.stdout.write(s*int(n)+'\n')
