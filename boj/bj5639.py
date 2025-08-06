import sys

sys.setrecursionlimit(20000)

inputs = sys.stdin.readlines()
pre_order = list(map(int, inputs))
root = pre_order[0]
tree = {root: [-1, -1]}
stack = list()
cur = root

for new_num in pre_order[1:]:
    if new_num < cur:
        tree[cur][0] = new_num
        tree[new_num] = [-1, -1]
        stack.append(cur)
        cur = new_num
    else:
        while len(stack) > 0 and stack[-1] < new_num:
            cur = stack.pop()
        # print(new_num, "is", cur, "'s child")
        tree[cur][1] = new_num
        tree[new_num] = [-1, -1]
        cur = new_num


def dfs(tree, cur):
    if cur in tree and tree[cur][0] > 0:
        dfs(tree, tree[cur][0])
    if cur in tree and tree[cur][1] > 0:
        dfs(tree, tree[cur][1])
    print(cur)


# list(map(lambda x: print(f"{x} : child={tree[x]}"), tree))
dfs(tree, root)
