import sys
inputs = sys.stdin.readlines()
t = int(inputs[0])
idx = 1
for _ in range(t):
    yy = 0
    kk = 0
    for _ in range(9):
        y, k = map(int, inputs[idx].rstrip().split())
        yy += y
        kk += k
        idx += 1
    if yy > kk:
        print("Yonsei")
    elif yy < kk:
        print("Korea")
    else:
        print("Draw")
