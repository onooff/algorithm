import sys
inputs = sys.stdin.readlines()

for s in inputs:
    upper, lower, num, space = 0, 0, 0, 0
    for c in s:
        if c == '\n':
            break

        if c.isalpha():
            if c.islower():
                lower += 1
            else:
                upper += 1
        elif c.isdigit():
            num += 1
        else:
            space += 1
    print(lower, upper, num, space)
