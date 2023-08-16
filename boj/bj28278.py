import sys

inputs = sys.stdin.readlines()

stk = list()
ans = list()
for i in range(1, len(inputs)):
    if inputs[i][0] == "1":
        stk.append(inputs[i].split()[1])
    elif inputs[i][0] == "2":
        if len(stk) > 0:
            ans.append(stk.pop())
        else:
            ans.append("-1")
    elif inputs[i][0] == "3":
        ans.append(str(len(stk)))
    elif inputs[i][0] == "4":
        if len(stk) > 0:
            ans.append("0")
        else:
            ans.append("1")
    elif inputs[i][0] == "5":
        if len(stk) > 0:
            ans.append(stk[-1])
        else:
            ans.append("-1")

print("\n".join(ans))
