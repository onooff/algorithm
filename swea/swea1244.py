def dfs(s, c, max, d):
    tmp = int(''.join(s))
    if c > 0 and tmp in d:
        for i in range(c):
            tmp = d[tmp]
        return tmp

    if c == 0:
        if tmp > max:
            return tmp
        else:
            return max

    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            s[i], s[j] = s[j], s[i]
            tmp2 = int(''.join(s))
            if tmp2 > tmp:
                max = dfs(s, c-1, max, d)
            s[i], s[j] = s[j], s[i]
        if max in d:
            return max
    return max


t = int(input())

for tc in range(1, t+1):
    n, c = map(int, input().split())
    s = list(str(n))
    # print(s)
    d = dict()
    tmp = sorted(s)
    tmp.reverse()
    m1 = int(''.join(tmp))
    if (len(tmp) >= 3 and tmp[len(tmp)-2] != tmp[len(tmp)-3]) or len(tmp) < 3:
        tmp[len(tmp)-1], tmp[len(tmp)-2] = tmp[len(tmp)-2], tmp[len(tmp)-1]
    m2 = int(''.join(tmp))
    d.setdefault(m1, m2)
    d.setdefault(m2, m1)

    ans = dfs(s, c, n, d)

    print('#', tc, ' ', ans, sep='')
