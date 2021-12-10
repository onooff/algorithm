import sys
inputs = sys.stdin.readlines()
s = inputs[0].rstrip()

ll_head = [None, None, None]
cur = ll_head
for c in s:
    nxt = [None, c, None]
    nxt[0] = cur
    cur[2] = nxt
    cur = nxt

for i in range(2, len(inputs)):
    if inputs[i][0] == 'L':
        if cur[0] != None:
            cur = cur[0]
    elif inputs[i][0] == 'D':
        if cur[2] != None:
            cur = cur[2]
    elif inputs[i][0] == 'B':
        if cur[1] != None:
            cur = cur[0]
            if cur[2][2] != None:
                cur[2][2][0] = cur
            cur[2] = cur[2][2]
    elif inputs[i][0] == 'P':
        new = [None, inputs[i][2], None]
        new[0] = cur
        new[2] = cur[2]
        if cur[2] != None:
            cur[2][0] = new
        cur[2] = new
        cur = new
cur = ll_head[2]
while cur != None:
    sys.stdout.write(cur[1])
    cur = cur[2]
sys.stdout.write('\n')
