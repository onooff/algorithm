import sys
input = sys.stdin.readline

c, n = map(int, input().rstrip().split())

color = dict()
for _ in range(c):
    s = input().rstrip()
    cur = color
    for ch in s:
        cur.setdefault(ch, dict())
        cur = cur[ch]
    cur.setdefault("end", None)

nick = dict()
for _ in range(n):
    s = input().rstrip()
    cur = nick
    for ch in s:
        cur.setdefault(ch, dict())
        cur = cur[ch]
    cur.setdefault("end", None)

q = int(input())
for _ in range(q):
    s = input().rstrip()
    col = color
    nic = nick
    yes = False
    nick_chk = False
    for i in range(len(s)):
        if nick_chk:
            yes = True
            for j in range(i, len(s)):
                ch = s[j]
                if ch not in nic:
                    yes = False
                    break
                nic = nic[ch]
            if "end" not in nic:
                yes = False
            if yes:
                break
            nick_chk = False
            nic = nick
        ch = s[i]
        if ch not in col:
            break

        col = col[ch]
        if "end" in col:
            nick_chk = True
    if yes:
        print("Yes")
    else:
        print("No")
