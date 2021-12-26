s = input()

maxx = list()
tmp = list()
for i in range(len(s) - 1, -1, -1):
    if s[i] == "K":
        maxx.append("".join(tmp))
        tmp = ["5"]
    else:
        if len(tmp) > 0:
            tmp.append("0")
        else:
            maxx.append("1")
maxx.append("".join(tmp))
print("".join(reversed(maxx)))

minn = list()
cnt = 0
for i in range(len(s) + 1):
    if i == len(s) or s[i] == "K":
        if cnt > 0:
            minn.append("1")
            cnt -= 1
        for _ in range(cnt):
            minn.append("0")
        if i < len(s):
            minn.append("5")
        cnt = 0
    else:
        cnt += 1
print("".join(minn))
