def solution(n, k, cmd):
    ans = ['O' for i in range(n)]
    nu = dict()
    nd = dict()
    stack = list()
    for i in range(n):
        nu.setdefault(i, i-1)
        nd.setdefault(i, i+1)
    for c in cmd:
        if c[0] == 'U':
            for i in range(int(c[2:])):
                if nu[k] == -1:
                    break
                else:
                    k = nu[k]
        elif c[0] == 'D':
            for i in range(int(c[2:])):
                if nd[k] == n:
                    break
                else:
                    k = nd[k]
        elif c[0] == 'C':
            stack.append((k, nu[k], nd[k]))
            nd[nu[k]] = nd[k]
            nu[nd[k]] = nu[k]
            ans[k] = 'X'
            if nd[k] == n:
                k = nu[k]
            else:
                k = nd[k]
        elif c[0] == 'Z':
            r = stack.pop()
            nd[r[1]] = r[0]
            nu[r[2]] = r[0]
            ans[r[0]] = 'O'
    answer = ''.join(ans)
    return answer
