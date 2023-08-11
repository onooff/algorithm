import sys

inputs = sys.stdin.readlines()
stk = list()
ans = list()

for i in range(1, len(inputs)):
    cmd = inputs[i].rstrip().split()
    if cmd[0] == "push":
        stk.append(cmd[1])
    elif cmd[0] == "pop":
        if len(stk) == 0:
            ans.append("-1")
        else:
            ans.append(stk.pop())
    elif cmd[0] == "size":
        ans.append(str(len(stk)))
    elif cmd[0] == "empty":
        if len(stk) == 0:
            ans.append("1")
        else:
            ans.append("0")
    elif cmd[0] == "top":
        if len(stk) == 0:
            ans.append("-1")
        else:
            ans.append(stk[-1])

print("\n".join(ans))
