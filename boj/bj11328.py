import sys
inputs = sys.stdin.readlines()
for i in range(1, len(inputs)):
    tmp = inputs[i].split()
    a = list(tmp[0])
    b = list(tmp[1])
    a.sort()
    b.sort()
    ans = True
    for j in range(len(a)):
        if a[j] != b[j]:
            ans = False
            break
    if ans:
        print("Possible")
    else:
        print("Impossible")
