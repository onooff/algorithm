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
            sys.stdout.write("-1\n")
        else:
            sys.stdout.write(q[idx]+"\n")
            idx += 1
    elif command[0] == "size":
        sys.stdout.write(str(len(q)-idx)+"\n")
    elif command[0] == "empty":
        if idx >= len(q):
            sys.stdout.write("1\n")
        else:
            sys.stdout.write("0\n")
    elif command[0] == "front":
        if idx >= len(q):
            sys.stdout.write("-1\n")
        else:
            sys.stdout.write(q[idx]+"\n")
    elif command[0] == "back":
        if idx >= len(q):
            sys.stdout.write("-1\n")
        else:
            sys.stdout.write(q[len(q)-1]+"\n")


'''
#1등코드
from sys import stdin, stdout

class Queue:
    def __init__(self, maxsize):
        self._data = [0] * maxsize
        self._front = 0
        self._rear = 0
    def push(self, n):
        self._data[self._rear] = n
        self._rear += 1
    def pop(self):
        if not self.empty():
            p = self._data[self._front]
            self._front += 1
            return p
        return -1
    def size(self):
        return self._rear - self._front
    def empty(self):
        return self.size() == 0
    def front(self):
        if not self.empty():
            return self._data[self._front]
        return -1
    def back(self):
        if not self.empty():
            return self._data[self._rear - 1]
        return -1

N = int(stdin.readline())
queue = Queue(N)
for _ in range(N):
    cmd, *v = stdin.readline().split()
    if cmd == 'push':
        queue.push(int(v[0]))
    elif cmd == 'pop':
        stdout.write(str(queue.pop()) + '\n')
    elif cmd == 'size':
        stdout.write(str(queue.size()) + '\n')
    elif cmd == 'empty':
        stdout.write(str(1 if queue.empty() else 0) + '\n')
    elif cmd == 'front':
        stdout.write(str(queue.front()) + '\n')
    elif cmd == 'back':
        stdout.write(str(queue.back()) + '\n')
'''
