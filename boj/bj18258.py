import sys
inputs = sys.stdin.readlines()

n = int(inputs[0])
q = list()
idx = 0
for i in range(1, len(inputs)):
    command = list(inputs[i].rstrip().split())
    if command[0] == "push":
        q.append(command[1])
    elif command[0] == "pop":
        if idx >= len(q):
            print(-1)
        else:
            print(q[idx])
            idx += 1
    elif command[0] == "size":
        print(len(q)-idx)
    elif command[0] == "empty":
        if idx >= len(q):
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if idx >= len(q):
            print(-1)
        else:
            print(q[idx])
    elif command[0] == "back":
        if idx >= len(q):
            print(-1)
        else:
            print(q[len(q)-1])
