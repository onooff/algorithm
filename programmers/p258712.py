def solution(friends, gifts):
    name_to_i = {s: i for i, s in enumerate(friends)}
    l = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    g = [0 for i in range(len(friends))]
    ans = [0 for i in range(len(friends))]
    for gg in gifts:
        a, b = map(lambda x: name_to_i[x], gg.split())
        l[a][b] += 1
        g[a] += 1
        g[b] -= 1
    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            if l[i][j] != l[j][i]:
                if l[i][j] > l[j][i]:
                    ans[i] += 1
                else:
                    ans[j] += 1
            else:
                if g[i] > g[j]:
                    ans[i] += 1
                elif g[i] < g[j]:
                    ans[j] += 1
    return max(ans)
