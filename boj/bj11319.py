import sys
inputs = sys.stdin.readlines()
find = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
for i in range(1, len(inputs)):
    cnt = {True: 0, False: 0}
    for j in range(len(inputs[i])-1):
        if inputs[i][j] != ' ':
            cnt[inputs[i][j] in find] += 1
    print(cnt[False], cnt[True])
