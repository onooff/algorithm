import sys
inputs = sys.stdin.readlines()
for num in inputs:
    num = int(num)
    x = 1
    while x < num or x % num != 0:
        x *= 10
        x += 1
    print(len(str(x)))
