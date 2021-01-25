n = int(input())

for a in range(n-1):
    for b in range(n-1-a):
        print(' ', end='')
    print('*', end='')
    for b in range((a*2)-1):
        print(' ', end='')
    if a > 0:
        print('*', end='')
    print()
for a in range((n*2)-1):
    print('*', end='')
