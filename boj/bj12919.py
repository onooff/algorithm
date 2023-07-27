a = input()
b = input()

q = [b]
nq = []
while len(q) > 0 and len(q[0]) != len(a):
    cur = q.pop()
    if cur[0] == "B":
        nq.append(cur[1:][::-1])
    if cur[-1] == "A":
        nq.append(cur[:-1])

    if len(q) == 0:
        q = nq
        nq = []

ans = 0
for s in q:
    if s == a:
        ans = 1
        break
print(ans)
