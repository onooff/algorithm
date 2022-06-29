n = int(input())
parent = list(map(int, input().split()))
leaves = {i for i in range(n)}
child_cnt = [0 for i in range(n)]
root = -1
for i in range(n):
    leaves.discard(parent[i])
    if parent[i] == -1:
        root = i
    child_cnt[parent[i]] += 1
cut = int(input())
if root == cut:
    print(0)
else:
    leaf_cnt = [0 for i in range(n)]
    for leaf in leaves:
        cur = leaf
        while cur != -1:
            leaf_cnt[cur] += 1
            cur = parent[cur]

    if child_cnt[parent[cut]] == 1:
        print(leaf_cnt[root])
    else:
        print(leaf_cnt[root]-leaf_cnt[cut])
