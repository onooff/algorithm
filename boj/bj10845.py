import sys

inputs = sys.stdin.readlines()
q = list()
ans = list()

for i in range(1, len(inputs)):
    cmd = inputs[i].rstrip().split()
    if cmd[0] == "push":
        q.append(cmd[1])
    elif cmd[0] == "pop":
        if len(q) == 0:
            ans.append("-1")
        else:
            ans.append(q.pop(0))
    elif cmd[0] == "size":
        ans.append(str(len(q)))
    elif cmd[0] == "empty":
        if len(q) == 0:
            ans.append("1")
        else:
            ans.append("0")
    elif cmd[0] == "front":
        if len(q) == 0:
            ans.append("-1")
        else:
            ans.append(q[0])
    elif cmd[0] == "back":
        if len(q) == 0:
            ans.append("-1")
        else:
            ans.append(q[-1])

print("\n".join(ans))
