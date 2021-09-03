def solution(sales, links):
    inf = 999999999
    tree = dict()
    manager = [-1 for i in range(len(sales))]
    for l in links:
        l[0] -= 1
        l[1] -= 1
        tree.setdefault(l[0], set())
        tree[l[0]].add(l[1])
        manager[l[1]] = l[0]
    # print(tree)
    dp = [[0, sales[i]] for i in range(len(sales))]
    answer = 0

    q = [0]
    idx = 0
    while idx < len(q):
        cur = q[idx]
        idx += 1
        if cur in tree:
            for mem in tree[cur]:
                q.append(mem)

    q.reverse()

    for n in q:
        if n in tree:
            min_val = inf
            for child in tree[n]:
                if dp[child][1] > dp[child][0]:
                    dp[n][0] += dp[child][0]
                    dp[n][1] += dp[child][0]
                    min_val = min(min_val, dp[child][1]-dp[child][0])
                else:
                    dp[n][0] += dp[child][1]
                    dp[n][1] += dp[child][1]
                    min_val = 0
            dp[n][0] += min_val
    # print(dp)
    # for n in q:
    #     print(n+1,end=',')
    return min(dp[0][1], dp[0][0])
