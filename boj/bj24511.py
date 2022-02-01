input()
is_stack = list(map(int, input().split()))
l = list(map(int, input().split()))
input()
c = list(map(int, input().split()))

q = list()
for i in range(len(is_stack)):
    if is_stack[i] == 0:
        q.append(l[i])
q.reverse()

idx = 0
for n in c:
    q.append(n)
    print(q[idx], end=' ')
    idx += 1
