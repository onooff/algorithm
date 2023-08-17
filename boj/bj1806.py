import sys

input = sys.stdin.readline

n, s = map(int, input().split())
l = list(map(int, input().rstrip().split()))

h = -1
e = -1
summ = 0
minn_len = float("inf")
while True:
    if summ < s:
        h += 1
        if h >= len(l):
            break
        summ += l[h]
    else:
        minn_len = min(minn_len, h - e)
        e += 1
        summ -= l[e]
    # print(e, h, summ, "★" if summ >= s else "")
if summ >= s:
    minn_len = min(minn_len, h - e)

if minn_len == float("inf"):
    print(0)
else:
    print(minn_len)
