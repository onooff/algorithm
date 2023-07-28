import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    s = input()
    k = int(input())

    d = dict()
    for i in range(len(s)):
        c = s[i]
        d.setdefault(c, list())
        d[c].append(i)

    # print(">>>", d)
    minn = float("inf")
    maxx = -1
    for c in d:
        if len(d[c]) >= k:
            for i in range(k - 1, len(d[c])):
                # print(">>>", c, d[c][i] - d[c][i - k + 1] + 1)
                minn = min(minn, d[c][i] - d[c][i - k + 1] + 1)
                maxx = max(maxx, d[c][i] - d[c][i - k + 1] + 1)
    if maxx == -1:
        print(-1)
    else:
        print(minn, maxx)
