import sys
inputs = sys.stdin.readlines()
v = {'a', 'e', 'i', 'o', 'u'}
for i in range(len(inputs)-1):
    s = inputs[i]
    cnt = 0
    for c in s:
        if c.lower() in v:
            cnt += 1
    sys.stdout.write(str(cnt)+'\n')
