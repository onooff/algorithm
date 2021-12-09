import sys
inputs = sys.stdin.readlines()
for i in range(1, len(inputs)):
    a, b, c = map(int, inputs[i].rstrip().split())
    chk = b-c
    if chk == a:
        print("does not matter")
    elif chk > a:
        print("advertise")
    else:
        print("do not advertise")
