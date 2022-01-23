t = int(input())
for _ in range(t):
    l = input()
    head = list()
    tail = list()
    for c in l:
        if c == "<":
            if len(head) > 0:
                tail.append(head.pop())
        elif c == ">":
            if len(tail) > 0:
                head.append(tail.pop())
        elif c == "-":
            if len(head) > 0:
                head.pop()
        else:
            head.append(c)
    print(''.join(head)+''.join(reversed(tail)))
