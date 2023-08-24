import sys

inputs = sys.stdin.readlines()


def isprime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


answer = list()
for i in range(1, len(inputs)):
    n = int(inputs[i])

    while True:
        if isprime(n):
            answer.append(n)
            break
        n += 1
print(*answer, sep="\n")
