import sys
inputs = sys.stdin.readlines()

d = {
    '0': 5,
    '1': 3,
    '2': 4,
    '3': 4,
    '4': 4,
    '5': 4,
    '6': 4,
    '7': 4,
    '8': 4,
    '9': 4
}

for i in range(len(inputs)-1):
    ans = 1
    for c in inputs[i].rstrip():
        ans += d[c]
    sys.stdout.write(f"{ans}\n")
