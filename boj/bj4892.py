import sys
inputs = sys.stdin.readlines()
odd_or_even = {0: "even", 1: "odd"}
for i in range(len(inputs)-1):
    num = int(inputs[i])
    n = num*3
    oe = n % 2
    if oe == 1:
        n += 1
    n //= 2
    n *= 3
    n //= 9
    sys.stdout.write(f'{i+1}. {odd_or_even[oe]} {n}\n')
