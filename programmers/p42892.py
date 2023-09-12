import sys

sys.setrecursionlimit(10**6)


def dfs(cur, g, answer):
    answer[0].append(cur)
    if g[cur][0] != -1:
        dfs(g[cur][0], g, answer)
    if g[cur][1] != -1:
        dfs(g[cur][1], g, answer)
    answer[1].append(cur)


def solution(nodeinfo):
    answer = [[], []]
    sorted_nodes = []
    for i in range(len(nodeinfo)):
        sorted_nodes.append((-nodeinfo[i][1], nodeinfo[i][0], i + 1))
    sorted_nodes.sort(key=lambda x: x)

    g = {x: None for x in range(1, len(nodeinfo) + 1)}
    # [left,right,parent, x]
    root = sorted_nodes[0][2]
    g[root] = [-1, -1, -1, sorted_nodes[0][1]]

    parent_level_nodes = []
    cur_level_nodes = [sorted_nodes[0]]
    plns = set()
    for i in range(1, len(sorted_nodes)):
        cur = sorted_nodes[i]
        if cur_level_nodes[0][0] != cur[0]:
            parent_level_nodes = cur_level_nodes
            cur_level_nodes = []
            plns = {x[2] for x in parent_level_nodes}
        cur_level_nodes.append(cur)

        find = root
        while find not in plns:
            if cur[1] < g[find][3]:
                find = g[find][0]
            elif cur[1] > g[find][3]:
                find = g[find][1]

        g[cur[2]] = [-1, -1, find, cur[1]]
        if cur[1] < g[find][3]:
            g[find][0] = cur[2]
        elif cur[1] > g[find][3]:
            g[find][1] = cur[2]

    dfs(root, g, answer)
    return answer


# print(
#     solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]])
# )
