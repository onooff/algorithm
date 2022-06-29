n = int(input())
l = list(map(int, input().split()))
tree = dict()
loot = -1
for i in range(len(l)):
    tree.setdefault(i, set())
    if l[i] == -1:
        loot = i
    else:
        tree.setdefault(l[i], set())
        tree[l[i]].add(i)

cut = int(input())

q = [loot]
nq = list()
idx = 0
ans = 0
while idx < len(q):
    cur = q[idx]
    idx += 1
    if cur != cut:
        if len(tree[cur]) == 0:
            ans += 1
        else:
            is_ans = True
            for nxt in tree[cur]:
                if nxt == cut:
                    continue
                is_ans = False
                nq.append(nxt)
            if is_ans:
                ans += 1
    if idx >= len(q):
        q = nq
        nq = list()
        idx = 0
print(ans)
