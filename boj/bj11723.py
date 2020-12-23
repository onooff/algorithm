import sys
input = sys.stdin.readline

n = int(input())
s = [False]*20
for i in range(n):
    command = input().strip().split()
    # print(command)
    c = command[0][:2]
    # print(c)
    if len(command) >= 2:
        x = int(command[1])-1
    if c == 'ad':
        s[x] = True
    elif c == 're':
        s[x] = False
    elif c == 'ch':
        if s[x]:
            print(1)
        else:
            print(0)
    elif c == 'to':
        # print(s[x], not s[x])
        s[x] = not s[x]
    elif c == 'al':
        s = [True]*20
    elif c == 'em':
        s = [False]*20
