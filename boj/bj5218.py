import sys
print = sys.stdout.write

inputs = sys.stdin.readlines()
for i in range(1, len(inputs)):
    a, b = inputs[i].rstrip().split()
    print("Distances:")
    for j in range(len(a)):
        d = ord(b[j])-ord(a[j])
        if d < 0:
            d += 26
        print(' ')
        print(str(d))
    print('\n')
