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

nick = set()
for _ in range(n):
    nick.add(input().rstrip())

q = int(input())
for _ in range(q):
    s = input().rstrip()
    col = color
    yes = False
    for i in range(len(s)):
        ch = s[i]
        if ch not in col:
            break

        col = col[ch]
        if "end" in col:
            if i < len(s)-1 and s[i+1:] in nick:
                yes = True
                break
    if yes:
        print("Yes")
    else:
        print("No")
