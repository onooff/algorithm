string = input()
stack = list()
ans = list()
for c in string:
    if c == "*" or c == "/":
        while len(stack) > 0 and (
            stack[-1] != "+" and stack[-1] != "-" and stack[-1] != "("
        ):
            ans.append(stack.pop())
        stack.append(c)
    elif c == "+" or c == "-":
        while len(stack) > 0 and stack[-1] != "(":
            ans.append(stack.pop())
        stack.append(c)
    elif c == "(":
        stack.append(c)
    elif c == ")":
        while len(stack) > 0 and stack[-1] != "(":
            ans.append(stack.pop())
        if len(stack) > 0 and stack[-1] == "(":
            stack.pop()
    else:
        ans.append(c)
while len(stack) > 0:
    ans.append(stack.pop())

print("".join(ans))
