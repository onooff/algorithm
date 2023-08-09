n = int(input())
a = list(input())
b = list(input())


def flip(l, x):
    if 0 <= x < len(l):
        for i in range(x - 1, x + 2):
            if 0 <= i < len(l):
                if l[i] == "0":
                    l[i] = "1"
                else:
                    l[i] = "0"


inf = float("inf")
ans = inf
for tryy in range(2):
    cnt = 0
    tmp = list(a)
    if tryy == 1:
        cnt += 1
        flip(tmp, 0)
    for i in range(n):
        if tmp[i] != b[i]:
            cnt += 1
            flip(tmp, i + 1)
    if "".join(tmp) == "".join(b):
        ans = min(ans, cnt)

if ans == inf:
    ans = -1
print(ans)
