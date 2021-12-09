import sys

op = {
    '@': lambda x: x*3,
    '%': lambda x: x+5,
    '#': lambda x: x-7,
}

inputs = sys.stdin.readlines()
for i in range(1, len(inputs)):
    inputs[i] = inputs[i].rstrip().split()
    n = float(inputs[i][0])
    for j in range(1, len(inputs[i])):
        n = op[inputs[i][j]](n)
    print(f"{n:.2f}")
