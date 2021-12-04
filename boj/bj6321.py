import sys
inputs = sys.stdin.readlines()
n = int(inputs[0])
for i in range(1, len(inputs)):
    l = list(inputs[i].rstrip())
    for j in range(len(l)):
        asci = ord(l[j])
        if asci == 90:
            asci = 64
        l[j] = chr(asci+1)
    sys.stdout.write(f"String #{i}\n{''.join(l)}")
    if i != n:
        sys.stdout.write("\n\n")
