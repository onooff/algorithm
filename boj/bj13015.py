n = int(input())
space = ''
for i in range(n-2):
    space += ' '
space += '*'

for _ in range(n):
    print("*", end='')
for _ in range((n-2)*2+1):
    print(" ", end='')
for _ in range(n):
    print("*", end='')
print()

for i in range(n-1):
    if i == n-2:
        for _ in range(i+1):
            print(" ", end='')
        print("*", end=space[:-1])
        for _ in range(((n-2)*2+1)-2*(i+1)):
            print(" ", end='')
        print("*", end=space+"\n")
        continue
    for _ in range(i+1):
        print(" ", end='')
    print("*", end=space)
    for _ in range(((n-2)*2+1)-2*(i+1)):
        print(" ", end='')
    print("*", end=space+"\n")

for i in range(n-3, -1, -1):
    for _ in range(i+1):
        print(" ", end='')
    print("*", end=space)
    for _ in range(((n-2)*2+1)-2*(i+1)):
        print(" ", end='')
    print("*", end=space+"\n")

for _ in range(n):
    print("*", end='')
for _ in range((n-2)*2+1):
    print(" ", end='')
for _ in range(n):
    print("*", end='')
print()
