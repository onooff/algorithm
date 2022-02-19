import sys
inputs = sys.stdin.readlines()
for i in range(1, len(inputs)):
    name, point = inputs[i].split()
    sys.stdout.write(name)
    point = int(point)
    if 97 <= point:
        sys.stdout.write(" A+\n")
    elif 90 <= point:
        sys.stdout.write(" A\n")
    elif 87 <= point:
        sys.stdout.write(" B+\n")
    elif 80 <= point:
        sys.stdout.write(" B\n")
    elif 77 <= point:
        sys.stdout.write(" C+\n")
    elif 70 <= point:
        sys.stdout.write(" C\n")
    elif 67 <= point:
        sys.stdout.write(" D+\n")
    elif 60 <= point:
        sys.stdout.write(" D\n")
    else:
        sys.stdout.write(" F\n")
